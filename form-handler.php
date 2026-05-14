<?php
/**
 * Prime Appliance Repair – Booking Form Handler
 * Handles two form layouts:
 *   1. Inner-page mini-form: name, phone, zip, appliance, issue
 *   2. Full booking page:    fname, lname, phone, email, address,
 *                            appliance, brand, date, time, issue
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

/* ── Rate-limit: 1 submission per IP per 60 s ── */
session_start();
$now = time();
if (isset($_SESSION['last_submit']) && ($now - $_SESSION['last_submit']) < 60) {
    http_response_code(429);
    echo json_encode(['ok'=>false,'error'=>'Please wait a moment before submitting again.']);
    exit;
}

/* ── Honeypot: bots fill it, humans don't see it ── */
if (!empty($_POST['website'])) {
    echo json_encode(['ok'=>true]); // silent block
    exit;
}

/* ── Sanitise helper ── */
function clean($v) {
    return htmlspecialchars(strip_tags(trim($v ?? '')), ENT_QUOTES, 'UTF-8');
}

/* ── Collect fields — support both form layouts ── */
// Name: full booking page sends fname+lname; mini-form sends name
$fname     = clean($_POST['fname']     ?? '');
$lname     = clean($_POST['lname']     ?? '');
$full_name = clean($_POST['name']      ?? '');
if (!$fname && !$lname && $full_name) {
    // Mini-form: split "John Smith" → fname=John, lname=Smith
    $parts = explode(' ', $full_name, 2);
    $fname = $parts[0];
    $lname = $parts[1] ?? '';
}

$phone     = clean($_POST['phone']     ?? '');
$email     = clean($_POST['email']     ?? '');
$address   = clean($_POST['address']   ?? '');
$zip       = clean($_POST['zip']       ?? ''); // mini-form fallback
$appliance = clean($_POST['appliance'] ?? '');
$brand     = clean($_POST['brand']     ?? '');
$date      = clean($_POST['date']      ?? '');
$time      = clean($_POST['time']      ?? '');
$issue     = clean($_POST['issue']     ?? '');

// Location: full form uses address; mini-form uses zip
$location = $address ?: ($zip ? "Zip: {$zip}" : '');

/* ── Validation ── */
if (!$fname || !$phone || !$appliance || !$issue) {
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
$display_name = trim("{$fname} {$lname}");
$to      = 'appliancerepairserviceus@gmail.com';
$subject = "New Booking Request – {$appliance} – {$display_name}";

$body  = "=== NEW APPOINTMENT REQUEST ===\n\n";
$body .= "Name:       {$display_name}\n";
$body .= "Phone:      {$phone}\n";
$body .= "Email:      " . ($email    ?: '(not provided)') . "\n";
$body .= "Location:   " . ($location ?: '(not provided)') . "\n\n";
$body .= "Appliance:  {$appliance}\n";
$body .= "Brand:      " . ($brand ?: '(not provided)') . "\n";
$body .= "Date:       " . ($date  ?: 'Flexible') . "\n";
$body .= "Time:       " . ($time  ?: 'Any time') . "\n\n";
$body .= "Problem Description:\n{$issue}\n\n";
$body .= "---\n";
$body .= "Submitted: " . date('Y-m-d H:i:s T') . "\n";
$body .= "IP: " . ($_SERVER['REMOTE_ADDR'] ?? 'unknown') . "\n";

/* ── Headers ── */
$from    = 'booking@appliancerepairclovis.com';
$headers  = "From: Prime Booking <{$from}>\r\n";
$headers .= "Reply-To: " . ($email ? "{$display_name} <{$email}>" : $from) . "\r\n";
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
