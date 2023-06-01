program main{
	var i,n,x : int;
	begin;
		write("factorial for");
		x:=1;
		n:=5;	
		for (i:=1;i<n;i++){
			x := x * i;
		}
		write(x);
	end;
}