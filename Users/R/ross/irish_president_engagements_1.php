<?php
date_default_timezone_set('Europe/Dublin');

// Get the most recently scraped date from the DB
// $max = strtotime(scraperwiki::select('date FROM swdata ORDER by date DESC LIMIT 1'));
// If none start in 1970
if(!$max) $max = 0;

// Scrape the page with the list of weeks for that year
$html = scraperwiki::scrape('http://president.ie/index.php?section=6&lang=eng&year=1997');
//Fetch all the week IDs 
preg_match_all('/engagement=([0-9]{5,7})/',$html,$dates);

// Fetch all the week start dates
preg_match_all('|Week beginning ([a-z0-9 ]{10,30})</a>|i',$html,$first);

// Work from the start of the year forwards to today
krsort($dates[1]);

// Loop through the weeks and scrape pages
foreach($dates[1] as $key => $week) {
    // Make week beginning date into unix time
    $f = strtotime($first[1][$key]);
    // Deduce if this is new information
    if($max < $f) {
        // Scrape the engagements from the given week
        $html = scraperwiki::scrape('http://president.ie/index.php?section=6&engagement='.$week.'&lang=eng');
        // Split into different days
        preg_match_all('|<dt><strong>([a-z0-9, ]{10,30})</strong></dt>|i',$html,$days);
        preg_match_all('|<dd>([\s\S]*?)</dd>|i',$html,$events);
        // Loop through different days in the given week
        foreach($days[1] as $i => $day) {
            // Scrape the various events on each day
            preg_match_all('|([0-9]{1,2}:[0-9]{1,2}) ([apm.]{2,4}):? (.*?)<br />|i',$events[1][$i],$timeplace);
            preg_match_all('|</strong>(.*?)</p>|i',$events[1][$i],$info);
            $hours = $timeplace[1];
            $apm = $timeplace[2];
            $place = $timeplace[3];
            // Loop through the events, tidy and save
            foreach($info[1] as $k => $item) {
                // Get a UNIX compatable timestamp
                $timestring = $day.' '.$hours[$k].$apm[$k];
                $date = strtotime($timestring);
                $data['date'] = gmdate('Y-m-d',$date);
                $data['time'] = gmdate('H:i',$date);
                $data['place'] = strip_tags($place[$k]);
                $data['place'] = utf8_encode($data['place']);
                $data['info'] = strip_tags($item);
                scraperwiki::save_sqlite(array('date','time'),$data);
                print_r($data);
            }
        }
    }
}
?>
<?php
date_default_timezone_set('Europe/Dublin');

// Get the most recently scraped date from the DB
// $max = strtotime(scraperwiki::select('date FROM swdata ORDER by date DESC LIMIT 1'));
// If none start in 1970
if(!$max) $max = 0;

// Scrape the page with the list of weeks for that year
$html = scraperwiki::scrape('http://president.ie/index.php?section=6&lang=eng&year=1997');
//Fetch all the week IDs 
preg_match_all('/engagement=([0-9]{5,7})/',$html,$dates);

// Fetch all the week start dates
preg_match_all('|Week beginning ([a-z0-9 ]{10,30})</a>|i',$html,$first);

// Work from the start of the year forwards to today
krsort($dates[1]);

// Loop through the weeks and scrape pages
foreach($dates[1] as $key => $week) {
    // Make week beginning date into unix time
    $f = strtotime($first[1][$key]);
    // Deduce if this is new information
    if($max < $f) {
        // Scrape the engagements from the given week
        $html = scraperwiki::scrape('http://president.ie/index.php?section=6&engagement='.$week.'&lang=eng');
        // Split into different days
        preg_match_all('|<dt><strong>([a-z0-9, ]{10,30})</strong></dt>|i',$html,$days);
        preg_match_all('|<dd>([\s\S]*?)</dd>|i',$html,$events);
        // Loop through different days in the given week
        foreach($days[1] as $i => $day) {
            // Scrape the various events on each day
            preg_match_all('|([0-9]{1,2}:[0-9]{1,2}) ([apm.]{2,4}):? (.*?)<br />|i',$events[1][$i],$timeplace);
            preg_match_all('|</strong>(.*?)</p>|i',$events[1][$i],$info);
            $hours = $timeplace[1];
            $apm = $timeplace[2];
            $place = $timeplace[3];
            // Loop through the events, tidy and save
            foreach($info[1] as $k => $item) {
                // Get a UNIX compatable timestamp
                $timestring = $day.' '.$hours[$k].$apm[$k];
                $date = strtotime($timestring);
                $data['date'] = gmdate('Y-m-d',$date);
                $data['time'] = gmdate('H:i',$date);
                $data['place'] = strip_tags($place[$k]);
                $data['place'] = utf8_encode($data['place']);
                $data['info'] = strip_tags($item);
                scraperwiki::save_sqlite(array('date','time'),$data);
                print_r($data);
            }
        }
    }
}
?>
<?php
date_default_timezone_set('Europe/Dublin');

// Get the most recently scraped date from the DB
// $max = strtotime(scraperwiki::select('date FROM swdata ORDER by date DESC LIMIT 1'));
// If none start in 1970
if(!$max) $max = 0;

// Scrape the page with the list of weeks for that year
$html = scraperwiki::scrape('http://president.ie/index.php?section=6&lang=eng&year=1997');
//Fetch all the week IDs 
preg_match_all('/engagement=([0-9]{5,7})/',$html,$dates);

// Fetch all the week start dates
preg_match_all('|Week beginning ([a-z0-9 ]{10,30})</a>|i',$html,$first);

// Work from the start of the year forwards to today
krsort($dates[1]);

// Loop through the weeks and scrape pages
foreach($dates[1] as $key => $week) {
    // Make week beginning date into unix time
    $f = strtotime($first[1][$key]);
    // Deduce if this is new information
    if($max < $f) {
        // Scrape the engagements from the given week
        $html = scraperwiki::scrape('http://president.ie/index.php?section=6&engagement='.$week.'&lang=eng');
        // Split into different days
        preg_match_all('|<dt><strong>([a-z0-9, ]{10,30})</strong></dt>|i',$html,$days);
        preg_match_all('|<dd>([\s\S]*?)</dd>|i',$html,$events);
        // Loop through different days in the given week
        foreach($days[1] as $i => $day) {
            // Scrape the various events on each day
            preg_match_all('|([0-9]{1,2}:[0-9]{1,2}) ([apm.]{2,4}):? (.*?)<br />|i',$events[1][$i],$timeplace);
            preg_match_all('|</strong>(.*?)</p>|i',$events[1][$i],$info);
            $hours = $timeplace[1];
            $apm = $timeplace[2];
            $place = $timeplace[3];
            // Loop through the events, tidy and save
            foreach($info[1] as $k => $item) {
                // Get a UNIX compatable timestamp
                $timestring = $day.' '.$hours[$k].$apm[$k];
                $date = strtotime($timestring);
                $data['date'] = gmdate('Y-m-d',$date);
                $data['time'] = gmdate('H:i',$date);
                $data['place'] = strip_tags($place[$k]);
                $data['place'] = utf8_encode($data['place']);
                $data['info'] = strip_tags($item);
                scraperwiki::save_sqlite(array('date','time'),$data);
                print_r($data);
            }
        }
    }
}
?>
<?php
date_default_timezone_set('Europe/Dublin');

// Get the most recently scraped date from the DB
// $max = strtotime(scraperwiki::select('date FROM swdata ORDER by date DESC LIMIT 1'));
// If none start in 1970
if(!$max) $max = 0;

// Scrape the page with the list of weeks for that year
$html = scraperwiki::scrape('http://president.ie/index.php?section=6&lang=eng&year=1997');
//Fetch all the week IDs 
preg_match_all('/engagement=([0-9]{5,7})/',$html,$dates);

// Fetch all the week start dates
preg_match_all('|Week beginning ([a-z0-9 ]{10,30})</a>|i',$html,$first);

// Work from the start of the year forwards to today
krsort($dates[1]);

// Loop through the weeks and scrape pages
foreach($dates[1] as $key => $week) {
    // Make week beginning date into unix time
    $f = strtotime($first[1][$key]);
    // Deduce if this is new information
    if($max < $f) {
        // Scrape the engagements from the given week
        $html = scraperwiki::scrape('http://president.ie/index.php?section=6&engagement='.$week.'&lang=eng');
        // Split into different days
        preg_match_all('|<dt><strong>([a-z0-9, ]{10,30})</strong></dt>|i',$html,$days);
        preg_match_all('|<dd>([\s\S]*?)</dd>|i',$html,$events);
        // Loop through different days in the given week
        foreach($days[1] as $i => $day) {
            // Scrape the various events on each day
            preg_match_all('|([0-9]{1,2}:[0-9]{1,2}) ([apm.]{2,4}):? (.*?)<br />|i',$events[1][$i],$timeplace);
            preg_match_all('|</strong>(.*?)</p>|i',$events[1][$i],$info);
            $hours = $timeplace[1];
            $apm = $timeplace[2];
            $place = $timeplace[3];
            // Loop through the events, tidy and save
            foreach($info[1] as $k => $item) {
                // Get a UNIX compatable timestamp
                $timestring = $day.' '.$hours[$k].$apm[$k];
                $date = strtotime($timestring);
                $data['date'] = gmdate('Y-m-d',$date);
                $data['time'] = gmdate('H:i',$date);
                $data['place'] = strip_tags($place[$k]);
                $data['place'] = utf8_encode($data['place']);
                $data['info'] = strip_tags($item);
                scraperwiki::save_sqlite(array('date','time'),$data);
                print_r($data);
            }
        }
    }
}
?>
