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
