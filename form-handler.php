<?php
/**
 * Prime Appliance Repair – Booking Form Handler
 * Receives POST from booking form, sends email via PHP mail()
 * Returns JSON: {"ok":true} or {"ok":false,"error":"..."}
 */

header('Content-Type: application/json');
header('Access-Control-Allow-Origin: https://appliancerepairclovis.com');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

/* ── Only accept POST ── */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['ok'=>false,'error'=>'Method not allowed']);
    exit;
}

/* ── Rate-limit: 1 submission per IP per 60 s (uses session) ── */
session_start();
$now = time();
if (isset($_SESSION['last_submit']) && ($now - $_SESSION['last_submit']) < 60) {
    http_response_code(429);
    echo json_encode(['ok'=>false,'error'=>'Please wait a moment before submitting again.']);
    exit;
}

/* ── Honeypot: a hidden field bots fill in ── */
if (!empty($_POST['website'])) {
    // Silently succeed so bots don't know they were blocked
    echo json_encode(['ok'=>true]);
    exit;
}

/* ── Sanitise helper ── */
function clean($v) {
    return htmlspecialchars(strip_tags(trim($v ?? '')), ENT_QUOTES, 'UTF-8');
}

/* ── Collect fields ── */
$fname    = clean($_POST['fname']    ?? '');
$lname    = clean($_POST['lname']    ?? '');
$phone    = clean($_POST['phone']    ?? '');
$email    = clean($_POST['email']    ?? '');
$address  = clean($_POST['address']  ?? '');
$appliance= clean($_POST['appliance']?? '');
$brand    = clean($_POST['brand']    ?? '');
$date     = clean($_POST['date']     ?? '');
$time     = clean($_POST['time']     ?? '');
$issue    = clean($_POST['issue']    ?? '');

/* ── Basic validation ── */
if (!$fname || !$lname || !$phone || !$address || !$appliance || !$issue) {
    http_response_code(400);
    echo json_encode(['ok'=>false,'error'=>'Please fill in all required fields.']);
    exit;
}
if ($email && !filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['ok'=>false,'error'=>'Please enter a valid email address.']);
    exit;
}

/* ── Build email ── */
$to      = 'appliancerepairserviceus@gmail.com';
$subject = "New Booking Request – {$appliance} – {$fname} {$lname}";

$body  = "=== NEW APPOINTMENT REQUEST ===\n\n";
$body .= "Name:       {$fname} {$lname}\n";
$body .= "Phone:      {$phone}\n";
$body .= "Email:      " . ($email ?: '(not provided)') . "\n";
$body .= "Address:    {$address}\n\n";
$body .= "Appliance:  {$appliance}\n";
$body .= "Brand:      " . ($brand ?: '(not provided)') . "\n";
$body .= "Date:       " . ($date  ?: 'Flexible') . "\n";
$body .= "Time:       " . ($time  ?: 'Any time') . "\n\n";
$body .= "Problem Description:\n{$issue}\n\n";
$body .= "---\n";
$body .= "Submitted: " . date('Y-m-d H:i:s T') . "\n";
$body .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

/* ── Headers: set Reply-To to customer email if provided ── */
$from    = 'booking@appliancerepairclovis.com';
$headers  = "From: Prime Booking <{$from}>\r\n";
$headers .= "Reply-To: " . ($email ? "{$fname} {$lname} <{$email}>" : $from) . "\r\n";
$headers .= "MIME-Version: 1.0\r\n";
$headers .= "Content-Type: text/plain; charset=UTF-8\r\n";
$headers .= "X-Mailer: PHP/" . phpversion() . "\r\n";

/* ── Send ── */
$sent = mail($to, $subject, $body, $headers);

if ($sent) {
    $_SESSION['last_submit'] = $now;
    echo json_encode(['ok'=>true]);
} else {
    http_response_code(500);
    echo json_encode(['ok'=>false,'error'=>'Mail delivery failed. Please call us at (559) 765-0303.']);
}
