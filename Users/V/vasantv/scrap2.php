<?php

//scrapping html
require 'scraperwiki/simple_html_dom.php';           

for($id=800000;$id<=899999;$id +=1)
{

    $dom = new simple_html_dom();
    //sourcing html
    //$id = 937789;
    $html = scraperWiki::scrape("http://www.mciindia.org/ViewDetails.aspx?ID=".$id);
               
    
    $dom->load($html);

    foreach($dom->find("table bgColor='#f0f0f0' tr") as $data){
        $tds = $data->find("td class='tdrow'");
        if(trim($tds[0]->plaintext) != "" && trim($tds[1]->plaintext)!="") 
        {
            $record = array('id'=>$id, 'field' => $tds[0]->plaintext,'value' => $tds[1]->plaintext);
            print ($id);
            //print_r($record);
            scraperwiki::save_sqlite(array("id","field"),$record,"IndiaDocs",0);
        }
    }
    
    $dom->__destruct();
}
?>
<?php

//scrapping html
require 'scraperwiki/simple_html_dom.php';           

for($id=800000;$id<=899999;$id +=1)
{

    $dom = new simple_html_dom();
    //sourcing html
    //$id = 937789;
    $html = scraperWiki::scrape("http://www.mciindia.org/ViewDetails.aspx?ID=".$id);
               
    
    $dom->load($html);

    foreach($dom->find("table bgColor='#f0f0f0' tr") as $data){
        $tds = $data->find("td class='tdrow'");
        if(trim($tds[0]->plaintext) != "" && trim($tds[1]->plaintext)!="") 
        {
            $record = array('id'=>$id, 'field' => $tds[0]->plaintext,'value' => $tds[1]->plaintext);
            print ($id);
            //print_r($record);
            scraperwiki::save_sqlite(array("id","field"),$record,"IndiaDocs",0);
        }
    }
    
    $dom->__destruct();
}
?>
