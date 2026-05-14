<?php
/**
 * Prime Appliance Repair – Booking Form Handler
 * Sends via Gmail SMTP (STARTTLS port 587) — bypasses nginx cache issue
 * Returns JSON: {"ok":true} or {"ok":false,"error":"..."}
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST')    { http_response_code(405); echo json_encode(['ok'=>false]); exit; }

/* ── Gmail credentials ── */
$gmail_user = 'appliancerepairserviceus@gmail.com';
$gmail_pass = 'uygkqotqmpexeaxk';   // App Password (spaces stripped)
$recipient  = 'appliancerepairserviceus@gmail.com';

/* ── Honeypot ── */
$raw  = file_get_contents('php://input');
$data = json_decode($raw, true) ?: $_POST;
if (!empty($data['website']) || !empty($_POST['website'])) {
    echo json_encode(['ok'=>true]); exit;
}

/* ── Sanitise helper ── */
function clean($v) {
    return htmlspecialchars(strip_tags(trim($v ?? '')), ENT_QUOTES, 'UTF-8');
}

/* ── Collect fields — handles both form layouts ── */
$fname     = clean($_POST['fname']     ?? $data['fname']     ?? '');
$lname     = clean($_POST['lname']     ?? $data['lname']     ?? '');
$full_name = clean($_POST['name']      ?? $data['name']      ?? '');
if (!$fname && $full_name) {
    $parts = explode(' ', $full_name, 2);
    $fname = $parts[0]; $lname = $parts[1] ?? '';
}
$phone     = clean($_POST['phone']     ?? $data['phone']     ?? '');
$email     = clean($_POST['email']     ?? $data['email']     ?? '');
$address   = clean($_POST['address']   ?? $data['address']   ?? '');
$zip       = clean($_POST['zip']       ?? $data['zip']       ?? '');
$appliance = clean($_POST['appliance'] ?? $data['appliance'] ?? '');
$brand     = clean($_POST['brand']     ?? $data['brand']     ?? '');
$date      = clean($_POST['date']      ?? $data['date']      ?? '');
$time      = clean($_POST['time']      ?? $data['time']      ?? '');
$issue     = clean($_POST['issue']     ?? $data['issue']     ?? '');
$location  = $address ?: ($zip ? "Zip: $zip" : '');

/* ── Validation ── */
if (!$fname || !$phone || !$appliance || !$issue) {
    http_response_code(400);
    echo json_encode(['ok'=>false,'error'=>'Please fill in all required fields.']);
    exit;
}

/* ── Build email body ── */
$display_name = trim("$fname $lname");
$subject = "New Booking — $appliance — $display_name";
$body    = "=== NEW APPOINTMENT REQUEST ===\n\n"
         . "Name:       $display_name\n"
         . "Phone:      $phone\n"
         . "Email:      " . ($email    ?: '(not provided)') . "\n"
         . "Location:   " . ($location ?: '(not provided)') . "\n\n"
         . "Appliance:  $appliance\n"
         . "Brand:      " . ($brand ?: '(not provided)') . "\n"
         . "Date:       " . ($date  ?: 'Flexible') . "\n"
         . "Time:       " . ($time  ?: 'Any time') . "\n\n"
         . "Problem:\n$issue\n\n"
         . "---\n"
         . "Submitted: " . date('Y-m-d H:i:s T') . "\n"
         . "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

/* ── Gmail SMTP over STARTTLS port 587 ── */
function send_gmail($user, $pass, $to, $subject, $body) {
    $sock = @fsockopen('smtp.gmail.com', 587, $errno, $errstr, 15);
    if (!$sock) return "connect_failed: $errstr";
    stream_set_timeout($sock, 15);

    $read = function() use ($sock) {
        $out = '';
        while (!feof($sock)) {
            $line = fgets($sock, 512);
            $out .= $line;
            if (isset($line[3]) && $line[3] === ' ') break;
        }
        return $out;
    };
    $cmd = function($c) use ($sock, $read) { fwrite($sock, "$c\r\n"); return $read(); };
    $ok  = function($r, $code='250') { return strpos($r, $code) !== false; };

    $read(); // banner
    $cmd('EHLO appliancerepairclovis.com');
    $r = $cmd('STARTTLS');
    if (!$ok($r, '220')) { fclose($sock); return "starttls_failed: $r"; }
    if (!stream_socket_enable_crypto($sock, true, STREAM_CRYPTO_METHOD_TLS_CLIENT))
        { fclose($sock); return "tls_failed"; }
    $cmd('EHLO appliancerepairclovis.com');
    $cmd('AUTH LOGIN');
    $cmd(base64_encode($user));
    $r = $cmd(base64_encode($pass));
    if (!$ok($r, '235')) { fclose($sock); return "auth_failed: $r"; }

    $cmd("MAIL FROM:<$user>");
    $cmd("RCPT TO:<$to>");
    $cmd('DATA');

    $headers  = "From: Prime Booking <$user>\r\n";
    $headers .= "To: $to\r\n";
    $headers .= "Reply-To: $user\r\n";
    $headers .= "Subject: $subject\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
    $headers .= "\r\n";

    $r = $cmd($headers . $body . "\r\n.");
    $cmd('QUIT');
    fclose($sock);
    return $ok($r) ? true : "data_failed: $r";
}

$result = send_gmail($gmail_user, $gmail_pass, $recipient, $subject, $body);

if ($result === true) {
    echo json_encode(['ok' => true]);
} else {
    error_log("[form-handler] Gmail SMTP failed: $result");
    http_response_code(500);
    echo json_encode(['ok'=>false,'error'=>'Could not send email. Please call us at (559) 765-0303.']);
}
