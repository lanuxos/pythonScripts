# EP5. Offline web scrapping
from bs4 import BeautifulSoup
content = '''
<!DOCTYPE html>




 



<html lang="la">

      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">
        <link rel="icon" href="/bcel/resources/imgs/favicon.ico">

        
   
          
        <link href="/bcel/resources/css/bootstrap.min.css" rel="stylesheet">
        <link href="/bcel/resources/css/font-awesome.min.css" rel="stylesheet">  
        <link href="/bcel/resources/css/glyphicons.css" rel="stylesheet">
        <link href="/bcel/resources/css/glyphicons-bootstrap.css" rel="stylesheet">
        
        <link href="/bcel/resources/css/styles.css" rel="stylesheet">
        <link href="/bcel/resources/css/datepicker.css" rel="stylesheet">
        <link href="/bcel/resources/css/fancybox.css" rel="stylesheet">
        <link href="/bcel/resources/css/infinite-slider.css" rel="stylesheet">
        <link href="/bcel/resources/css/slick.css" rel="stylesheet">
        <link href="/bcel/resources/css/slick-theme.css" rel="stylesheet">

      
        <script src="/bcel/resources/js/jquery.min.js"></script>
         <script src="/bcel/resources/js/slick.js"></script>
        <script src="/bcel/resources/js_data/carousel.js"></script>
          <script src="/bcel/resources/js_data/index.js"></script>
          
        
         
   

      <!--[if lt IE 9]>
	      <script src="/bcel/resources/js/html5shiv.min.js"></script>
	      <script src="/bcel/resources/js/respond.min.js"></script>
	      <script src="/bcel/resources/js/css3media.js"></script>
      <![endif]-->


	 





 
	  
     
  
  


    </head>
 
    <body >
    
    
    
    
     
    
    

        

        <div class="head-top" id="top">
            <div class="container">

                 

                <a href="bcel-news.html?fType=bcel-news&type=news" class="xs-hide ">ຂ່າວສານ</a>  
                <a href="bcel-career.html?Id=career" class="">ສະໝັກວຽກ</a> 
                <a href="form-download.html?Id=forms" class="xs-hide ">ແບບຟອມຕ່າງໆ</a> 
                <a href="promotion.html?pType=" class="">ກິດຈະກໍາ &amp; ໂປຼໂມຊັນ</a>      
				<a class="lghide " href="https://www.bcel.com.la:8443/" target="_blank">ອີເມວ </a>
     
    
      			
                
				
			  					
		                
		                
		                    
		               
		                    
		                        <a  href="https://www.bcel.com.la/bcel/exchange-rate.html?lang=en" class="lghide  ">EN</a>
		                    
		                  
		                    
				 
				 

            </div>
            
            

        </div> 


        <div class="navbar navbar-default  topnav" role="navigation">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>    
                </div>
                <span id="home"><a class="logo" href="/bcel/home.html">  <img src="/bcel/resources/imgs/logo.png" width="60" height="58" alt="Logo"  /></a><a class="navbar-brand" href="/bcel/home.html" id="mhide">ທະນາຄານ ການຄ້າຕ່າງປະເທດລາວ ມະຫາຊົນ</a></span>

                <div class="navbar-collapse collapse ">
                    <ul class="nav navbar-nav navbar-cen">


                        <li id="xhide"><a href="/bcel/home.html"><span class="glyphicons glyphicons-bank homebank"></span></a></li>

                        
                        <li class="dropdown mega-dropdown" id="dd1">

                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">ຜະລິດຕະພັນ &amp; ບໍລິການ <span class="chevron_toggleable1 fa fa-angle-down"></span></a>				
                            <div class="dropdown-menu mega-dropdown-menu">
                                <div class="container">
                                    
                                    <div class="row">

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 ">
                                            <ul class="tabmenu">

                                                <li><a href="product.html?prid=deposits" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-coins"></span>ເງິນຝາກ</a></li>
                                                <li><a href="product.html?prid=credits" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-money"></span>ສິນເຊື່ອ</a></li>
                                                <li><a href="product.html?prid=cards" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-credit-card"></span>ບັດ</a></li>

                                            </ul>
                                        </div>

                                        <div class="col-xs-12  col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">
                                                <li><a href="product.html?prid=e-banking" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-iphone-shake"></span>ບໍລິການ ເອເລັກໂທຣນິກ</a></li>
                                                <li><a href="product.html?prid=atm" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-modal-window"></span>ເອທີເອັມ</a></li>
                                                <li><a href="product.html?prid=ft" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-transfer"></span>ໂອນເງິນ </a></li>
                                            </ul>
                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">
                                                <li><a href="product.html?prid=tf" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-invoice"></span>ການຄ້າດ້ານການເງິນ</a></li>
                                                <li><a href="product.html?prid=utilities-payment" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-notes-2"></span>ຊຳລະສາທາລະນຸປະໂພກ</a></li>
                                                <li><a href="product.html?prid=other-service" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-tie"></span>ບໍລິການອື່ນໆ</a></li>

                                            </ul>
                                        </div>


                                    </div>


                                    

                                </div>				
                       </div>
                       
                        </li>

                        
                        <li class="dropdown mega-dropdown" id="dd2">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown">ການເປີດເຜີຍຂໍ້ມູນ  <span class="chevron_toggleable2 fa fa-angle-down"></span></a>				
                            <div class="dropdown-menu mega-dropdown-menu">
                                <div class="container">
                                    
                                    <div class="row tabpad">

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 ">
                                            <ul class="tabmenu">
                                                <li><a href="financail-report.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-list-alt"></span>ລາຍງານດ້ານການເງິນ</a></li>
                                                <li><a href="dividend-data.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-notes-2"></span>ເງິນປັນຜົນ</a></li>

                                            </ul>
                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">

                                                <li><a href="summary-business.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-list-alt"></span>ບົດສະຫຼຸບການເຄື່ອນໄຫວທຸລະກິດ </a></li>             
                                                <li><a href="stock.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-charts"></span>ລາຄາຮຸ້ນຍ້ອນຫລັງ </a></li>

                                            </ul>
                                        </div>

                                        <div class="col-xs-12  col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">
                                                <li><a href="financail-data.html?fid=market-announce" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-bullhorn"></span>ແຈ້ງຂ່າວການລົງທຶນ</a></li>  
                                                <li><a href="share-structure.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-flowchart"></span>ໂຄງສ້າງຜູ້ຖືຮຸ້ນ</a></li>

                                                
                                            </ul>
                                        </div>


                                    </div>


                                    

                                </div>				
                           </div>
                        </li>
                        

                        
                        <li class="dropdown mega-dropdown" id="dd3">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown"> ກ່ຽວກັບ ທຄຕລ <span class="chevron_toggleable3 fa fa-angle-down"></span></a>				
                            <div class="dropdown-menu mega-dropdown-menu">
                                <div class="container">
                                    
                                    <div class="row">
                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 ">
                                            <ul class="tabmenu">

                                                <li><a href="history.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-history"></span>ປະຫວັດຄວາມເປັນມາ</a></li>
                                                <li><a href="organize-chart.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-flowchart"></span>ໂຄງຮ່າງການຈັດຕັ້ງ </a></li>
                                                <li><a href="bcel-ceo.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-vcard"></span>ຄະນະບໍລິຫານ </a></li>

                                            </ul>
                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">
                                                <li><a href="local-partner.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-handshake"></span>ບໍລິສັດໃນເຄືອ</a></li>
                                                <li> <a href="bcel-award.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-cup"></span>ຜົນສຳເລັດ</a></li>
                                                <li><a href="bcel-slogan.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-education"></span>ຄຳຂວັນ ແລະ ເຄື່ອງໝາຍການຄ້າ</a></li>

                                            </ul>
                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">      
                                                <li><a href="bcel-news.html?fType=bcel-news&type=news" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-newspaper"></span>ຂ່າວສານ </a></li>
                                                <li><a href="bcel-activity.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-picture"></span>ກິດຈະກໍາຕ່າງໆ </a></li>
                                            </ul>
                                        </div>    


                                    </div>


                                    

                                </div>				
                           </div>
                        </li>



                        
                        <li class="dropdown mega-dropdown" id="dd4">
                            <a href="#" class="dropdown-toggle" data-toggle="dropdown"> ຕິດຕໍ່ພວກເຮົາ <span class="chevron_toggleable4 fa fa-angle-down"></span></a>				
                            <div class="dropdown-menu mega-dropdown-menu">
                                <div class="container">
                                    
                                    <div class="row">

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 ">
                                            <ul class="tabmenu">

                                                <li> <a href="contact-corporate.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-group"></span>ສໍານັກງານໃຫຍ່</a></li>
                                                <li><a href="list-branch.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-google-maps"></span>ສາຂາ ແລະ ໜ່ວຍບໍລິການ</a></li>
                                                
                                            </ul>

                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">


                                                <li><a href="inter-partner.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-global"></span>ທະນາຄານຕົວແທນຢູ່ຕ່າງປະເທດ </a></li>             
                                                 <li> <a href="aml.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-shield"></span><small>ພະແນກສະກັດກັ້ນການຟອກເງິນ</small></a></li>
                                        
                                            </ul>
                                        </div>

                                        <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4">
                                            <ul class="tabmenu">
                                             
                                                <li><a href="feedback.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-comments"></span>ຄຳຄິດເຫັນ </a></li>
                                             
                                                <li><a href="faq.html" data-toggle="collapse" data-target=".navbar-collapse"><span class="glyphicons glyphicons-conversation"></span>ຄໍາຖາມທີ່ຖາມເລື້ອຍໆ </a></li>
                                               
                                            </ul>
                                        </div>    


                                    </div>


                                    

                                </div>				
                          </div>
                        </li>



                    </ul>

                    <ul class="nav navbar-nav navbar-right ">


                        <li > 
                            <form action="search.html" class="search-form" >
                                <div class="form-group has-feedback">
                                    <label for="search" class="sr-only">Search</label>
                                    <input type="text" class="form-control " name="q" id="q"  placeholder="ຄົ້ນຫາ" >
                                    <span class="glyphicon glyphicon-search form-control-feedback"></span>
                                </div>
                            </form>
                        </li>

                        <li id="xhide">
                   
                   
                     
                    
                        
                         
                            
   
                            
                         
                                <a  href="https://www.bcel.com.la/bcel/exchange-rate.html?lang=en" class=""> <span id="langId" class="langbtn"> EN </span> </a>
                      
                            
                     
                           
                           
                     
                        </li>

                        <li class="dropdown right-dropdown" > 
                             
                            
                             <a href="#" class="dropdown-toggle " data-toggle="dropdown" role="button" >
                             <lable><i class="glyphicon glyphicon-lock "></i> <span>ເຂົ້າສູ່ລະບົບ</span></lable>
                             </a>
                            
                            <ul class="dropdown-menu" role="menu">

                                <li>

                                   <a href="https://www.bcel.com.la/bcelibank/index.jsp" target="_blank"> 
                                      <img src="/bcel/resources/imgs/ibank1.gif"  alt=""/ class="center-block">
                                    <br/>
                                   <button class="center-block btn_blue">ເຂົ້າສູ່ລະບົບ <span class="fa fa-angle-right fa-lg">  </span> </button>
                                   </a>	
                                   	
                                </li>
                                


                                <li>
                                    <a href="https://www.bcel.com.la:8083/index.php?lang=1" target="_blank">
                                        <img src="/bcel/resources/imgs/bcel1.gif"  alt="" class="center-block "/> 
                                       <br/>
                                        <button class="center-block btn_red">ເຂົ້າສູ່ລະບົບ<span class="fa fa-angle-right fa-lg">  </span> </button>
                                      </a>		
                                </li>
                                
                                <li>
                                     <a href="https://www.bcel.com.la:8083/reg.php?langid=1" target="_blank"><button class="center-block btn_red">ລົງທະບຽນ<span class="fa fa-angle-right fa-lg">  </span> </button></a>	
                                    <br/>
                              </li>
                              
  				    <li>
                                     <a href="Stmt-check.html"><button class="center-block btn_green">ກວດບັນຊີສໍາຮອງ <span class="fa fa-angle-right fa-lg">  </span> </button></a>	
                                    </li>
                               

                            </ul>
   						</li>


                    </ul>
                </div>
            </div> 


        </div>


        <div class="clrboth"></div>

        
        <div id="render-page">
        
             
	              
	             		

  







<script src="/bcel/resources/js_data/exchange_rate.js"></script>

   <title>ອັດຕາແລກປ່ຽນເງິນຕາ  | ທຄຕລ</title>

<div class="container margin-20" id="render-head">

    <div class="row">

        <div class="col-sm-9">



            <h3 class="title">ອັດຕາແລກປ່ຽນເງິນຕາ </h3>
            <hr>
            

 

<div class="row">
  <div class="col-md-4">
  <label class=""><strong>ປະຈໍາວັນທີ: 2021-05-13</strong></label>
  </div>
  
    <div class="col-md-4">
  			<label class="xred">ເລືອກ ວັນທີ: </label>
                <input  class="" maxlength="15" type="text"  id="datepicker"  value="2021-05-13" />
              </div>
                
  <div class="col-md-4">
  
 <label class="xred"> ຄັ້ງທີ:</label> 
  
     		<select class="" id="round">
     		      
     		       
     		      
     		      
     		       
     		          
     		         		<option value="1" selected>1</option>
     		          
     		          
     		       
     		       
     		       
     		     

			</select>
	
  
  </div>

</div>



             <div class="table-responsive" id="resp-tables">
            
		     <table class="table  table-striped cf" width="100%">
		      
		          <thead class="cf">

                        <tr class="bggrey">
                            <th rowspan="2"><b>ປະເພດສະກຸນເງິນ</b></th>
                            <th rowspan="2"><b>ປະເທດ</b></th>
                            <th rowspan="2"><b>ລະຫັດສະກຸນເງິນ</b></th>
                            <th colspan="3"><b><center> ອັດຕາຊື້</b>  </center></th>
                    <th  rowspan="2" align="right" ><center><b>ອັດຕາຂາຍ</b></center></th>
                    </tr>
                    <tr>
                        <td align="right" class="numeric2"><b>NOTE</b></td>
                        <td align="right" class="numeric2"><b>BILL</b></td>
                        <td align="right" class="numeric2"><b>EFT</b></td>
                    </tr>
                    </thead>
                    <tbody>
                    
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">US Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/USD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">USD 1-20 </td>
                            <td data-title="NOTE" align="right" >9.405</td>
                            <td data-title="BILL" align="right" >9.406</td>
                            <td data-title="EFT" align="right" >9.408</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >9.427</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">US Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/USD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">USD 50-100 </td>
                            <td data-title="NOTE" align="right" >9.406</td>
                            <td data-title="BILL" align="right" >9.406</td>
                            <td data-title="EFT" align="right" >9.408</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >9.427</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Thai Baht</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/THB.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">THB </td>
                            <td data-title="NOTE" align="right" >326,03</td>
                            <td data-title="BILL" align="right" >326,03</td>
                            <td data-title="EFT" align="right" >326,08</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >328,49</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Euro</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/EUR.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">EUR 1-20 </td>
                            <td data-title="NOTE" align="right" >11.422</td>
                            <td data-title="BILL" align="right" >11.423</td>
                            <td data-title="EFT" align="right" >11.425</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >11.479</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Euro</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/EUR.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">EUR 50-500 </td>
                            <td data-title="NOTE" align="right" >11.423</td>
                            <td data-title="BILL" align="right" >11.423</td>
                            <td data-title="EFT" align="right" >11.425</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >11.479</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Pound Sterling</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/GBP.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">GBP </td>
                            <td data-title="NOTE" align="right" >13.183</td>
                            <td data-title="BILL" align="right" >13.183</td>
                            <td data-title="EFT" align="right" >13.185</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >13.447</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Australian Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/AUD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">AUD </td>
                            <td data-title="NOTE" align="right" >7.314</td>
                            <td data-title="BILL" align="right" >7.314</td>
                            <td data-title="EFT" align="right" >7.316</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >7.459</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Canadian Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/CAD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">CAD </td>
                            <td data-title="NOTE" align="right" >7.458</td>
                            <td data-title="BILL" align="right" >7.458</td>
                            <td data-title="EFT" align="right" >7.460</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >7.607</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Japanese Yen</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/JPY.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">JPY </td>
                            <td data-title="NOTE" align="right" >85,34</td>
                            <td data-title="BILL" align="right" >85,34</td>
                            <td data-title="EFT" align="right" >85,4</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >87,05</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Swiss Franc</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/CHF.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">CHF </td>
                            <td data-title="NOTE" align="right" >9.879</td>
                            <td data-title="BILL" align="right" >9.879</td>
                            <td data-title="EFT" align="right" >9.881</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >10.077</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Renminbi Yuan</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/CNY.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">CNY </td>
                            <td data-title="NOTE" align="right" >1.481</td>
                            <td data-title="BILL" align="right" >1.481</td>
                            <td data-title="EFT" align="right" >1.483</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >1.500</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Danish Krone</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/DKK.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">DKK </td>
                            <td data-title="NOTE" align="right" >-</td>
                            <td data-title="BILL" align="right" >-</td>
                            <td data-title="EFT" align="right" >1.569</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >1.600</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Norwegian Krone</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/NOK.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">NOK </td>
                            <td data-title="NOTE" align="right" >-</td>
                            <td data-title="BILL" align="right" >-</td>
                            <td data-title="EFT" align="right" >1.179</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >1.202</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Swedish Krona</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/SEK.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">SEK </td>
                            <td data-title="NOTE" align="right" >-</td>
                            <td data-title="BILL" align="right" >-</td>
                            <td data-title="EFT" align="right" >1.170</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >1.193</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Singapore Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/SGD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">SGD </td>
                            <td data-title="NOTE" align="right" >6.939</td>
                            <td data-title="BILL" align="right" >6.939</td>
                            <td data-title="EFT" align="right" >6.941</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >7.077</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">HongKong Dollar</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/HKD.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">HKD </td>
                            <td data-title="NOTE" align="right" >-</td>
                            <td data-title="BILL" align="right" >-</td>
                            <td data-title="EFT" align="right" >1.305</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >1.331</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Vietnamese Dong</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/VND.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">VND </td>
                            <td data-title="NOTE" align="right" >-</td>
                            <td data-title="BILL" align="right" >-</td>
                            <td data-title="EFT" align="right" >0,4114</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >0,4196</td>
                        </tr>
                    
                        <tr>
                            <td data-title="ປະເພດສະກຸນເງິນ" align="left">Korean Won</td>
                            <td data-title="ປະເທດ" align="left"><img src="resources/imgs/flag/KRW.png" width="22" height="22" /></td>
                            <td data-title="ລະຫັດສະກຸນເງິນ" align="left">KRW </td>
                            <td data-title="NOTE" align="right" >7,89</td>
                            <td data-title="BILL" align="right" >7,89</td>
                            <td data-title="EFT" align="right" >7,94</td>
                        	<td data-title="ອັດຕາຂາຍ" align="right" >8,04</td>
                        </tr>
                     
                       
                    </tbody>
                </table>


            </div>

            


            <br/>  
            <b>BILL: </b>Sight bill, cashier&#39;s Check, Traveller&#39;s Check, Money Order, Postal Order(Mandate). 
            <br/>
            <b>EFT: </b>ໂອນເງິນຜ່ານອີເລັກໂທຣນິກ(Money Gram,BCEL ONE,I-BANK), ແລກປ່ຽນເງິນຕາຜ່ານບັນຊີ.
            <br/>
             <br/>

            
            <p><b>ໝາຍເຫດ:  </b>ອັດຕາແລກປ່ຽນແຕ່ລະສະກຸນຂ້າງເທີງນີ້ ອາດມີການປ່ຽນແປງໄດ້ຫຼາຍຄັ້ງໃນລະຫວ່າງວັນ ໂດຍທີ່ບໍ່ມີການແຈ້ງໃຫ້ຮູ້ລ່ວງໜ້າຖ້າ ທ່ານສາມາດຮູ້ອັດ ຕາແລກປ່ຽນໄດ້ ທີ່ www.bcel.com.la . ກະລຸນາຕິດຕໍ່ ຂະແໜງບໍລິຫານຊັບສິນ-ໜີ້ສິນ ໂທລະສັບ: (856-21) 262614 ເພື່ອຢືນຢັນອັດຕາແລກປ່ຽນເມື່ອມີການແລກປ່ຽນເກີນ USD 5,000 (ຫຼືທຽບເທົ່າ) ຫຼືສະກຸນເງິນທີ່ບໍ່ໄດ້ສະແດງອັດຕາແລກ ປ່ຽນຢູ່ຂ້າງເທິງນີ້.</p>
        </div>

        <div class="col-sm-3  blog-sidebar">
            <div class="sidebar-module sidebar-module-inset">

                <div class="list-group"> 
                    <span id=""><a href="exchange-rate.html" class="list-group-item active"> ອັດຕາແລກປ່ຽນເງິນຕາ</a></span>
                    <span id=""><a href="interest.html?fid=fx-rate" class="list-group-item">ດາວໂຫລດ ອັດຕາແລກປ່ຽນເງິນຕາ</a></span>
                    <span id=""><a href="interest.html?fid=deposit-interest" class="list-group-item">ອັດຕາດອກເບ້ຍເງິນຝາກ</a></span>
                    <span id=""><a href="interest.html?fid=loan-interest" class="list-group-item">ອັດຕາດອກເບ້ຍເງິນກູ້</a></span>
                    <span id=""><a href="interest.html?fid=other-fee" class="list-group-item">ອັດຕາຄ່າທຳນຽມຕ່າງໆແລະອື່ນໆ</a></span>
                    <span id=""><a href="calculator.html" class="list-group-item">ເຄື່ອງຄຳນວນອັດຕາຕ່າງໆ </a></span>

                </div>
            </div>
            
            



  


<div class="sidebar-module sidebar-module-inset">
    <h4>ແຊໜ້ານີ້</h4>
    <ol class="list-unstyled">
        
        


		
		
		 
		
		
		
		  
		
		  
		

		

  		<li><a href="http://twitter.com/home?status=https%3a%2f%2fwww.bcel.com.la%2fbcel%2fexchange-rate.html" title="Share on Twitter"  class="btn btn-twitter" onclick="window.open(this.href, 'windowName', 'width=500, height=600, left=50, top=50, scrollbars, resizable'); return false;" ><i class="fa fa-twitter"></i> Twitter</a></li>
        
        <li><a href="https://www.facebook.com/sharer/sharer.php?u=https%3a%2f%2fwww.bcel.com.la%2fbcel%2fexchange-rate.html" title="Share on Facebook" class="btn btn-facebook" onclick="window.open(this.href, 'windowName', 'width=500, height=600, left=50, top=50, scrollbars, resizable'); return false;" ><i class="fa fa-facebook"></i> Facebook</a></li>
        
        <li><a href="https://plus.google.com/share?url=https%3a%2f%2fwww.bcel.com.la%2fbcel%2fexchange-rate.html" title="Share on Google+"  class="btn btn-googleplus" onclick="window.open(this.href, 'windowName', 'width=500, height=600, left=50, top=50, scrollbars, resizable'); return false;" ><i class="fa fa-google-plus"></i> Google+</a></li>
        
        <li><a href="http://www.stumbleupon.com/submit?url=https%3a%2f%2fwww.bcel.com.la%2fbcel%2fexchange-rate.html" title="Share on StumbleUpon"  data-placement="top" class="btn btn-stumbleupon" onclick="window.open(this.href, 'windowName', 'width=500, height=650, left=50, top=50, scrollbars, resizable'); return false;" ><i class="fa fa-stumbleupon"></i> Stumbleupon</a></li>
         
        <li><a href="http://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fwww.bcel.com.la%2fbcel%2fexchange-rate.html&title=&summary=" title="Share on LinkedIn"  class="btn btn-linkedin" onclick="window.open(this.href, 'windowName', 'width=500, height=600, left=50, top=50, scrollbars, resizable'); return false;" > <i class="fa fa-linkedin"></i> LinkedIn</a></li>



    </ol>
</div>


        </div>

    </div>

</div>

<script src="/bcel/resources/js/bootstrap-datepicker.js"></script>
<script>

    $("#datepicker, #datepicker2").datepicker({
        format: 'yyyy-mm-dd',
        endDate: '+0d',
        autoclose: true
    });
    $('#datepicker, #datepicker2').on('changeDate', function(ev) {
        $(this).datepicker('hide');
    });

</script>      

  <script>
  		(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  				(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
 				 m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  					})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  			ga('create', 'UA-66067779-1', 'auto');
  			ga('send', 'pageview');

</script>


	             
             	
             
            

        </div>

        




        <div class="marketing-cen bgred">

            <div class="container-bcel"> 
                <div class="row pt-4 pb-5">
                    <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 text-center">
                        <a href="interest.html?fid=other-fee" ><span class="glyphicons glyphicons-circle-info whitebig top10"></span>
                            <p class="whitetop ">  ເບິ່ງລາຍລະອຽດເພີ່ມເຕີມ </p>
                        </a>
                    </div>
                    <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 text-center">
                        <a href="https://www.youtube.com/channel/UChYtViKbPLrgwXetxse3xFw" target="_blank" >
                            <span class="glyphicons glyphicons-play-button whitebig top10"></span>
                            <p class="whitetop "> ວີດີໂອໂຄສະນາຕ່າງໆ</p>
                        </a>
                    </div>
                    <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 text-center">
                        <span id="calculatorMenu" >
                            <a  href="calculator.html" >
                                <span class="glyphicons glyphicons-calculator whitebig top10"></span>
                                <p class="whitetop "> ເຄື່ອງຄຳນວນອັດຕາຕ່າງໆ </p>
                            </a></span>
                    </div>
                </div>
       		</div>
       </div>
            
  <div class="marketing-cen bggrey">
		<div class="container-bcel">
			<div class="row margin-partner pt-4 pb-2">
				     <section class="partner-logos slider">
									    <div class="slide padding-partner">
																<a href="http://lsc.gov.la/" target="_blank">
															        <img src="/bcel/resources/imgs/links/lsc-en.jpg"   class="pull-right" alt=""/>
															        </a>
															        
									    </div>
									    <div class="slide padding-partner">
									    			<a href="http://www.lsx.com.la/" target="_blank">
															        <img src="/bcel/resources/imgs/links/lsx.jpg"   class="pull-right" alt=""/>
															        </a>
															        
									    </div>
									    
									    <div class="slide padding-partner">
									     <a href="https://www.bcel-kt.com/" target="_blank">
															        <img src="/bcel/resources/imgs/links/bcel-kt.jpg"  class="pull-right" alt=""/>
															        </a>
															         
									    </div>
									    
									    <div class="slide padding-partner">
											<a href="https://www.bfl-bred.com/" target="_blank">
															        <img src="/bcel/resources/imgs/links/bfl.jpg"   class="pull-right" alt=""/>
															        </a>
										</div>					         
									    <div class="slide padding-partner">
									    <a href="http://www.laovietbank.com.la/vi/" target="_blank">
															        <img src="/bcel/resources/imgs/links/laoviet.jpg"   class="pull-right" alt=""/>
															        </a>
															         
									    
									    </div>
									    
									    <div class="slide padding-partner">
									    <a href="http://www.laochinabank.com/" target="_blank">
															        <img src="/bcel/resources/imgs/links/lcnb.jpg"   class="pull-right" alt=""/>
															        </a>
															         
									    </div>
									    
									    <div class="slide padding-partner">
									    <a href="http://www.laovietinsurance.com/" target="_blank">
															        <img src="/bcel/resources/imgs/links/lvi.jpg"   class="pull-right" alt=""/>
															        </a>
									    </div>
									
									  </section>
						   <br>
				     </div>
            
        </div> 
       </div>

        
        <footer>


            
            

            <div class="marketing left100 xs-hide">
                <div class="container-bcel">
                    <div class="row text-center">


                        <div class="col-xs-4">
                            <p class=""><strong>ກ່ຽວກັບ ທຄຕລ </strong></p>

                            <p class=""><a href="history.html">ປະຫວັດຄວາມເປັນມາ</a></p>
                            <p class=""><a href="organize-chart.html">ໂຄງຮ່າງການຈັດຕັ້ງ</a></p>
                            <p class=""><a href="bcel-ceo.html">ຄະນະບໍລິຫານ</a></p>
                            <p class=""><a href="bcel-award.html">ຜົນສຳເລັດ</a></p>
                            <p class=""><a href="bcel-activity.html">ກິດຈະກໍາຕ່າງໆ</a></p>
                            <p class=""><a href="bcel-slogan.html">ຄຳຂວັນ ແລະ ເຄື່ອງໝາຍການຄ້າ</a> </p>
                            <p class=""><a href="https://www.bcel.com.la:8443/" target="_blank">ອີເມວ </a></p>
                            <p class=""><a href="https://www.bcel.com.la/bcelnotifications/migration_guide_lao.html" target="_blank">ຍ້າຍໄປລະບົບ BCEL i-Bank V.3 </a></p>
                            
                        </div>

                        <div class="col-xs-4">


                            <p class=""><strong>ຜະລິດຕະພັນ</strong></p>

                            <p class=""><a href="product.html?prid=deposits">ເງິນຝາກ</a></p>
                            <p class=""><a href="products.html?prd=credits">ສິນເຊື່ອ</a></p>
                            <p class=""><a href="product.html?prid=cards">ບັດ</a></p>
                            <p class=""><a href="product.html?prid=e-banking">ບໍລິການ ເອເລັກໂທຣນິກ</a></p> 
                            <p class=""><a href="product.html?prid=atm">ເອທີເອັມ</a></p>
                            <p class=""><a href="product.html?prid=ft">ໂອນເງິນ</a></p>
                            <p class=""><a href="product.html?prid=tf">ການຄ້າດ້ານການເງິນ</a></p>
                            <p class=""><a href="products.html?prd=other-service">ບໍລິການອື່ນໆ</a></p>
                            

                        </div>
                        
                        <div class="col-xs-4">
                            <p class=""><strong>ຄົ້ນຫາ</strong></p>

                            <p class=""><a href="interest.html?fid=other-fee">ອັດຕາຄ່າທຳນຽມຕ່າງໆແລະອື່ນໆ</a> </p>
                            <p class=""><a href="calculator.html">ເຄື່ອງຄຳນວນ</a> </p>
                            <p class=""><a href="faq.html">ຄໍາຖາມທີ່ຖາມເລື້ອຍໆ</a> </p>

                             &nbsp;
                            <p class=""><strong>ຕິດຕໍ່ </strong></p>

                            <p class=""><a href="contact-corporate.html">ສໍານັກງານໃຫຍ່</a></p>
                            <p class=""><a href="list-branch.html">ສາຂາ ແລະ ໜ່ວຍບໍລິການ</a></p>
                            
                            <p class=""><a href="form-download.html?Id=forms">ດາວໂຫລດແບບຟອມຕ່າງໆ</a></p>

                        </div>



                    </div>
                </div>
            </div>

            <p class="pull-right"><a href="#top"><span class="glyphicons glyphicons-circle-arrow-top whitetop xlarge"></span></a></p>

            <hr>


 			<div class="container-bcel">
                <div class="row text-center">
                      <div class="col-xs-12 col-sm-3 col-md-1 col-lg-1 marg-top">
                        <h3  class="fontB">
                         
                      	    
                      	    	28,45M
                      	    
                          	
                         
                        </h3> 
                        <p class=""> ຜູ້ເຂົ້າຊົມ </p>
                    </div>
  


                    <div class="col-xs-12 col-sm-3 col-md-2 col-lg-2"> 
                        <span class="glyphicons glyphicons-earphone mlarge"></span>
                        <span class="fontB  c1555 ">1555</span>
                        <p class=""> ໂທ:(+856-21) 213200 </p>

                    </div>
                    
                    <div class="col-xs-12 col-sm-3 col-md-2 col-lg-2 ">
                        <span class=" glyphicons glyphicons-fax xlarge "></span>
                        <p class=""> ແຟັກ:(+856-21) 213202 </p>

                    </div>

                    <div class="col-xs-12 col-sm-3 col-md-2 col-lg-2 ">
                        <a href="mailto:bcelhqv@bcel.com.la">
                            <span class="glyphicons glyphicons-envelope xlarge"></span><br>
                        	<span class="">ອີເມວ ຫາ: bcelhqv@bcel.com.la</span>
                        </a>
                      
                    </div>
                    
                    
                    
                   
                    
                     <div class="col-xs-12 col-sm-3 col-md-1 col-lg-1">
                        <span id="commentMenu" >
                            <a class="" href="https://www.facebook.com/BCEL.Bank/" target="_blank"> 
                            <span class="fa fa-facebook-square xlarge"></span><br>
                                Facebook
                            </a>
                        </span>
                    </div>
                    
                   
                    
                    <div class="col-xs-12 col-sm-3 col-md-2 col-lg-1 ">
                        <span id="commentMenu" >
                            <a class="" href="https://www.youtube.com/channel/UChYtViKbPLrgwXetxse3xFw" target="_blank"> 
                            <span class="fa fa-youtube-play xlarge"></span><br>
                                Youtube
                            </a>
                        </span>
                    </div>
                      <div class="col-xs-12 col-sm-3 col-md-1 col-lg-1 ">
                        <span id="commentMenu" >
                            <a class="" href="feedback.html" > 
                            <span class="glyphicons glyphicons-comments xlarge"></span><br>
                                ຄຳຄິດເຫັນ
                            </a>
                        </span>
                    </div>
                    
                    <div class="col-xs-12 col-sm-3 col-md-3 col-lg-2 marg-cpr">
                        <p class="small " >Copyright &copy; 2015<br/> ​ທະນາຄານ ການຄ້າຕ່າງປະເທດລາວ ມະຫາຊົນ.	<br/>​ສະ​ຫງວນ​ລິ​ຂະ​ສິດ</p>
                    </div>

                </div>
                
                
                
                
            </div>


        </footer>



		
        

    




    
    

    <script src="/bcel/resources/js/bootstrap.min.js"></script>
    <script src="/bcel/resources/js/jquery.number.min.js"></script>
    <script src="/bcel/resources/js/dateFormat.min.js"></script>

    
    <script src="/bcel/resources/vendor/ie10-viewport-bug-workaround.js"></script>

    <script>

            $('#dd1').on('click', function() {
                $('.chevron_toggleable1').toggleClass('fa-angle-down fa-angle-up');
            });
            $('#dd2').on('click', function() {
                $('.chevron_toggleable2').toggleClass('fa-angle-down fa-angle-up');
            });
            $('#dd3').on('click', function() {
                $('.chevron_toggleable3').toggleClass('fa-angle-down fa-angle-up');
            });
            $('#dd4').on('click', function() {
                $('.chevron_toggleable4').toggleClass('fa-angle-down fa-angle-up');
            });
    </script>


    <script type="text/javscript">
        $(document).ready(function() {

        var isIE = navigator.userAgent.indexOf(' MSIE ') > -1;
        if(isIE) {
        $('.modal').removeClass('fade');
        }
        });
    </script>

<!--[if lt IE 9]>

<script type="text/javascript">
$('button').click(function(){
    document.location = $(this).parents('a').first().prop('href');
});
</script>

<![endif]-->


 



</body>
</html>

'''

data = BeautifulSoup(content, 'html.parser')
print(data)
print(type(data))