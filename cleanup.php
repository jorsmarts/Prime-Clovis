<?php
// One-time cleanup script — deletes WordPress, keeps wp-content/uploads
// Delete this file immediately after running

function rrmdir($dir) {
    if (!is_dir($dir)) return;
    $items = scandir($dir);
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') continue;
        $path = $dir . '/' . $item;
        if (is_dir($path)) {
            rrmdir($path);
            rmdir($path);
        } else {
            unlink($path);
        }
    }
}

$base = __DIR__;
$log  = [];

// --- Dirs to fully delete ---
$del_dirs = ['wp-admin', 'wp-includes'];
foreach ($del_dirs as $d) {
    $path = "$base/$d";
    if (is_dir($path)) {
        rrmdir($path);
        rmdir($path);
        $log[] = "DELETED dir: $d";
    } else {
        $log[] = "SKIP (not found): $d";
    }
}

// --- wp-content: delete everything EXCEPT uploads ---
$wpc = "$base/wp-content";
if (is_dir($wpc)) {
    $items = scandir($wpc);
    foreach ($items as $item) {
        if ($item === '.' || $item === '..') continue;
        if ($item === 'uploads') { $log[] = "KEEP: wp-content/uploads"; continue; }
        $path = "$wpc/$item";
        if (is_dir($path)) {
            rrmdir($path);
            rmdir($path);
            $log[] = "DELETED dir: wp-content/$item";
        } else {
            unlink($path);
            $log[] = "DELETED file: wp-content/$item";
        }
    }
}

// --- Root WP files to delete ---
$del_files = [
    'index.php','license.txt','readme.html','php_errorlog',
    'wp-activate.php','wp-blog-header.php','wp-comments-post.php',
    'wp-config-sample.php','wp-config.php','wp-cron.php',
    'wp-links-opml.php','wp-load.php','wp-login.php','wp-mail.php',
    'wp-settings.php','wp-signup.php','wp-trackback.php','xmlrpc.php',
    '.htaccess'
];
foreach ($del_files as $f) {
    $path = "$base/$f";
    if (file_exists($path)) {
        unlink($path);
        $log[] = "DELETED file: $f";
    }
}

// --- Self-delete ---
unlink(__FILE__);
$log[] = "DELETED self: cleanup.php";

echo "<pre>DONE\n\n" . implode("\n", $log) . "\n</pre>";
?>
