<?php
// Serves Dispatch Portal widget JS through our domain — hides molboi.com and API key from browser
header('Content-Type: application/javascript');
header('Cache-Control: public, max-age=3600');

$js = @file_get_contents('https://molboi.com/widget/dispatch-widget.js');
if ($js === false) { http_response_code(502); echo '/* widget unavailable */'; exit; }

// Inject config at the top so window.DispatchPortal is set before the widget reads it
$config = "window.DispatchPortal={apiKey:'sk_2be74d199c304c44ad7eddb10d1176bd',serverUrl:'https://molboi.com'};\n";

echo $config . $js;
