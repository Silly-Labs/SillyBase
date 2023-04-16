<h1 align="center">SillyBase</h1>
<p align="center"><i>The worst database you will ever come across.</i></p>
<h2 align="center">Build the interperter</h2>
<p align="center">The project is held together by a single Makefile and can be used to run the interperter as so:  </p>




    make sillybase






<h2 align="center">SillyScript: The SillyBase Programming Language</h2>
<p align="center"><i>This database comes with it's own programming language that.. isn't SQL!</i></p>
<h3 align="center">Make a new query and manage it</h3>
<p align="center">To create and alter the data of a new query, you'll need to define the table by writing:  </p>




    NEW QUERY (make a preferred name for your query)





<p align="center">To alter the data and see the data of a query, you'll need to call it by the address:</p>





    NEW QUERY Pennywise
    INSERT AT 0 Nickelsmart
    LOGS 0





<p align="center">It's a very tedious process, but you can just spam the "INSERT AT" and "LOGS" command to print more than 1 line as shown:</p>




    NEW QUERY Pennywise
    INSERT AT 0 Nickelsmart
    LOGS 0
    INSERT AT 0 Quarterintelligent
    LOGS 0
    INSERT AT 0 Coin-knowledge
    LOGS 0





<h3 align="center">Export data from your queries</h3>
<p align="center">You are able to export the queries from your .sib files to a static HTML file by simply writing the following at the end of the file:</p>




    NEW QUERY Goobin
    INSERT AT 0 Hey
    LOGS 0
    INSERT AT 0 Are-you
    LOGS 0
    INSERT AT 0 Goobin?
    LOGS 0
    SAVE FILE




<p align="center">Since we are only using one query in this project, you should get a static HTML file that would show the following:</p>




    <table>
      <tr>
        <td>Goobin?</td>
      </tr>
    </table>





<h3 align="center">Select objects as single variable.</h3>
<p align="center">You can assign an address to a 'select' variable that can be called by writing "SELECTED" in the places where you'd usually put in addressess, like so:
    
    
    
    
    NEW QUERY Wrong!
    NEW QUERY Wrong!
    NEW QUERY Right!
    
    SELECT 2
    LOGS SELECTED

    
    
    
    
