<?php

class Color
{
    public $red = 0;
    public $green = 0;
    public $blue = 0;
    public $alpha = 0;

    public function __construct($r,$g,$b,$a)
    {
      $this->red = $r;
      $this->green = $g;
      $this->blue = $b;
      $this->alpha = $a;
    }
}
$c = new Color(255,0,0,255)
var_dump($c);
 ?>
