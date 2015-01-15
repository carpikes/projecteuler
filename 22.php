<?php
    $f = file_get_contents("in/22.txt");

    $f = str_replace(array(' ',',','"',"\n"),";", $f);
    $a = explode(";",$f);

    $names = array();
    foreach($a as $n)
        if(strlen($n)>0)
            $names[] = strtolower($n);

    sort($names);

    $sum = 0;
    for($i=0;$i<count($names);$i++) {
        $score = 0;
        $name = $names[$i];
        for($l=0;$l<strlen($name);$l++)
            $score += ord($name[$l]) - ord('a')+1;
        $score *= $i+1;
        $sum += $score;
    }
    echo $sum."\n";
?>
