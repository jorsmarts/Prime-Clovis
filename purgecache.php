<?php
// Purge SiteGround dynamic cache and delete self
if (function_exists('sg_cachepress_purge_cache')) {
    sg_cachepress_purge_cache();
}
// Also try to clear via header trick
header("Cache-Control: no-cache, no-store, must-revalidate");
header("Pragma: no-cache");
header("Expires: 0");

// Delete self
unlink(__FILE__);
echo "Cache purged and script deleted.";
?>
