<?php

treemax("in/18.txt");
treemax("in/67.txt");

function treemax($filename)
{
    $tree=array();

    $file=file_get_contents($filename);
    $lines=explode("\n", $file);
    foreach($lines as $line) {
        $n = explode(" ", $line);
        
        $la = array();
        foreach($n as $num)
            if(ctype_digit($num))
                $la[] = (int)$num;

        if(count($la)>0)
            $tree[] = $la;
    }


    for($i=count($tree)-2;$i>=0;$i--) {
        $l1 = $tree[$i];
        $l2 = $tree[$i+1];

        for($j=0;$j<count($l1);$j++) {
            $e = $l1[$j];
            if($l2[$j]>$l2[$j+1])
                $e += $l2[$j];
            else
                $e += $l2[$j+1];
            $tree[$i][$j] = $e;
        }
    }

    echo $tree[0][0]."\n";
} 
?>
