<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');
if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') { http_response_code(204); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo json_encode(['ok'=>false]); exit; }

$gmail_user = 'appliancerepairserviceus@gmail.com';
$gmail_pass = 'uygkqotqmpexeaxk';
$recipient  = 'appliancerepairserviceus@gmail.com';

$raw  = file_get_contents('php://input');
$data = json_decode($raw, true) ?: $_POST;
if (!empty($data['website']) || !empty($_POST['website'])) { echo json_encode(['ok'=>true]); exit; }

function clean($v) { return htmlspecialchars(strip_tags(trim($v ?? '')), ENT_QUOTES, 'UTF-8'); }

$fname     = clean($_POST['fname']     ?? $data['fname']     ?? '');
$lname     = clean($_POST['lname']     ?? $data['lname']     ?? '');
$full_name = clean($_POST['full_name'] ?? $data['full_name'] ?? $_POST['name'] ?? $data['name'] ?? '');
if (!$fname && $full_name) { $parts = explode(' ', $full_name, 2); $fname = $parts[0]; $lname = $parts[1] ?? ''; }
$phone     = clean($_POST['phone']     ?? $data['phone']     ?? '');
$email     = clean($_POST['email']     ?? $data['email']     ?? '');
$appliance = clean($_POST['appliance'] ?? $data['appliance'] ?? $_POST['appliance_type'] ?? $data['appliance_type'] ?? '');
$issue     = clean($_POST['issue']     ?? $data['issue']     ?? $_POST['issue_description'] ?? $data['issue_description'] ?? '');
$zip       = clean($_POST['zip']       ?? $data['zip']       ?? $_POST['zip_code'] ?? $data['zip_code'] ?? '');
$date      = clean($_POST['date']      ?? $data['date']      ?? '');
$address   = clean($_POST['address']   ?? $data['address']   ?? $_POST['zip'] ?? $data['zip'] ?? '');

if (!$fname || !$phone || !$appliance || !$issue) {
    http_response_code(400);
    echo json_encode(['ok'=>false,'error'=>'Please fill in all required fields.']);
    exit;
}

$display_name = trim("$fname $lname");
$subject = "[Prime Appliance Repair Services Fresno] New Booking — $appliance — $display_name";
$body = "=== NEW APPOINTMENT REQUEST ===\nPrime Appliance Repair Services Fresno\n\n"
      . "Name:      $display_name\n"
      . "Phone:     $phone\n"
      . "Email:     " . ($email ?: '(not provided)') . "\n"
      . "Address:   " . ($address ?: '(not provided)') . "\n\n"
      . "Date:      " . ($date  ?: '(not selected)') . "\n\n"
      . "Appliance: " . ($appliance ?: '(not provided)') . "\n\n"
      . "Message:\n$issue\n\n"
      . "---\n"
      . "Submitted: " . date('Y-m-d H:i:s T') . "\n"
      . "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

$log = date('Y-m-d H:i:s') . " | $fname $lname | $phone | $appliance\n";

$sock = @fsockopen('smtp.gmail.com', 587, $errno, $errstr, 15);
if (!$sock) {
    $log .= "CONNECT FAILED: [$errno] $errstr\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    http_response_code(500);
    echo json_encode(['ok'=>false,'error'=>'Connection failed. Please call (559) 765-0303.']);
    exit;
}
stream_set_timeout($sock, 15);
$read = function() use ($sock) {
    $out = '';
    while (!feof($sock)) { $line = fgets($sock, 512); $out .= $line; if (isset($line[3]) && $line[3] === ' ') break; }
    return $out;
};
$cmd = function($c) use ($sock, $read) { fwrite($sock, "$c\r\n"); return $read(); };
$ok  = function($r, $code='250') { return strpos($r, $code) !== false; };

$read();
$cmd('EHLO appliancerepairclovis.com');
$r = $cmd('STARTTLS');
if (!$ok($r,'220')) {
    fclose($sock); $log .= "STARTTLS FAILED: $r\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    http_response_code(500); echo json_encode(['ok'=>false,'error'=>'SMTP error. Call (559) 765-0303.']); exit;
}
if (!@stream_socket_enable_crypto($sock, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
    fclose($sock); $log .= "TLS FAILED\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    http_response_code(500); echo json_encode(['ok'=>false,'error'=>'TLS error. Call (559) 765-0303.']); exit;
}
$cmd('EHLO appliancerepairclovis.com');
$cmd('AUTH LOGIN');
$cmd(base64_encode($gmail_user));
$r = $cmd(base64_encode($gmail_pass));
if (!$ok($r,'235')) {
    fclose($sock); $log .= "AUTH FAILED: $r\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    http_response_code(500); echo json_encode(['ok'=>false,'error'=>'Auth error. Call (559) 765-0303.']); exit;
}
$cmd("MAIL FROM:<$gmail_user>");
$cmd("RCPT TO:<$recipient>");
$cmd('DATA');
$msg  = "From: Prime Appliance Repair Services Fresno <$gmail_user>\r\nTo: $recipient\r\nReply-To: $gmail_user\r\n";
$msg .= "Subject: $subject\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n\r\n";
$r = $cmd($msg . $body . "\r\n.");
$cmd('QUIT');
fclose($sock);

if ($ok($r)) {
    $log .= "SMTP OK\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    echo json_encode(['ok'=>true]);
} else {
    $log .= "SMTP FAILED: $r\n";
    file_put_contents(__DIR__.'/php_errorlog', $log, FILE_APPEND|LOCK_EX);
    http_response_code(500);
    echo json_encode(['ok'=>false,'error'=>'Send failed. Please call (559) 765-0303.']);
}
