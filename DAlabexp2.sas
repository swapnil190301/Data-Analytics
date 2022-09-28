title "Descriptive Analysis on cholestrol based on weight status";
proc means data=sashelp.heart;
		class Weight_Status;
		var Cholesterol;
run;
TITLE"Histrogram Plot for cholestrol by weight status";
PROC univariate data=sashelp.heart;
		class Weight_Status;
		var Cholesterol;
		histogram Cholesterol;
		inset SKEWNESS KURTOSIS;
		
run;
TITLE"Box Plot for Cholestrol by Weight Status";
proc sgplot data=sashelp.heart;
		vbox Cholesterol/ category=Weight_Status;
run;

