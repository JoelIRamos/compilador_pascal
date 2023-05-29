program test {
  var x, y : int;
  var z : real;
  begin; 
    x := 5;
    y := 2;
    z := 3.14;
    
    write(x + y);
    write(x * z);
    
    if (x > y) then {
      write("x is greater than y");
    } else {
      write("x is not greater than y");
    }
    
    while (x > 0) do {
      write(x);
      x := x - 1;
    }
    
    for (i := 1; i <= 10; i++) {
        write(i);
    }
  end;
}