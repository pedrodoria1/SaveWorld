


			
			function validaAlerta()
			{
				document.getElementById('sucesso').style.display = "none";
				document.getElementById('erro').style.display = "none";
				

				if (document.getElementById('nome').value == "") 	

				{
					document.getElementById('erro').style.display = "flex";
				}
				if (document.getElementById('sobrenome').style.border == "")	

				{
					document.getElementById('erro').style.display = "flex";
				}



				if (document.getElementById('nome').value != "")  		

				{
					document.getElementById('erro').style.display = "none";
				}





				if  (document.getElementById('sobrenome').style.border != "")		

				{
					document.getElementById('erro').style.display = "none";
				}


			}
			


			function validaForm()
			{

				document.getElementById('nome').style.border = "";
				document.getElementById('sobrenome').style.border = "";			


				if (document.getElementById('nome').value == "")
				{
					document.getElementById('nome').style.border = "2px solid red";	
				}
				if(document.getElementById('sobrenome').value == "")
				{
					document.getElementById('sobrenome').style.border = "2px solid red";
				}

			}


