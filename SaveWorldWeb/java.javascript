			



		document.getElementById('sucesso').style.display = "none";
		document.getElementById('erro').style.display = "none";

		//document.getElementById('sucesso').style.visibility='visible';

			function validaForm()
			{

				document.getElementById('nome').style.border = "";
				document.getElementById('senha').style.border = "";			


				if (document.getElementById('nome').value == "")
				{
					document.getElementById('nome').style.border = "2px solid red";	
				}
				if(document.getElementById('senha').value == "")
				{
					document.getElementById('senha').style.border = "2px solid red";
				}

			}

			function validaAlerta()
			{
				//document.getElementById('sucesso').style.display = "none";
				//document.getElementById('erro').style.display = "none";
				

				if (document.getElementById('nome').value == "") 	
				{
					document.getElementById('erro').style.display = "block";
				}

				if (document.getElementById('senha').style.border == "")	
				{
					document.getElementById('erro').style.display = "block";
				}


				if (document.getElementById('nome').value != "")  	
				{
					document.getElementById('erro').style.display = "none";
				}

				if  (document.getElementById('senha').style.border != "")		
				{
					document.getElementById('erro').style.display = "none";
				}

			}
			


