<?php 

function pan($a,$b) {
    $c = $a * $b;

    $tx = str_split($c.$a.$b);
    $dup = array_unique(array_diff_assoc( $tx, array_unique( $tx ) ));

    return count($dup)==0 && !in_array('0', $tx);
}

$sum = 0;
for($i=1;$i<9999;$i++) {
    echo $i."\n";
    for($j=$i;$j<9999;$j++)
        if(pan($i,$j))
            $sum += $i*$j;
}
echo $sum."\n";
?>
