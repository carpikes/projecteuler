<?php
    $digits = array("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen");

    $tens = array("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety");
    
    $hundred = "hundred";
    $thousand = "thousand";
    $and = "and";

    $sum = 0;
    for($i=1; $i<=1000;$i++) {

        $name = "";

        if($i == 1000)
            $name = $digits[1] . $thousand;
        else {
            if($i>=100 && $i<1000)
                $name .= $digits[$i/100] . $hundred;

            if(strlen($name)>0 && $i%100 != 0)
                $name.=$and;
            if($i%100<20)
                $name .= $digits[$i % 100];
            else
                $name .= $tens[($i%100)/10].$digits[$i % 10];
        } 
        $sum+=strlen($name);
    }
    echo $sum."\n";
?>
