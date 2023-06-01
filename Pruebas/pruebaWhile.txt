program main{
	var i,n,x : int;
	begin;
		write("factorial while");
		n := 5;
		x := 1;
		while (n>=1) do
		{
			x := x * n;
			n--;
		}
		write(x);
	end;
}