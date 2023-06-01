program main{
	var a,b,x,y,i : int;
	begin;	
		write("prueba if");

		a := 5;
		b :=  a + 3;
		x := b +5;
		y := x + a;

		if( a>b) then
		{
			i := a*5+(b+4);
			write("caso true");
			write(a);
		}else
		{
			if(y<x) then
			{
				i := x * (b * y);
				write(x);
				write("if anidado");
			}else
			{
				write("ultimo caso");
			}
		}
		write(i);
	end;
}