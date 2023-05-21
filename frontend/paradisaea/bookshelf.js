function init_title(ti){
	var et=document.createElement("title");
  	et.innerHTML=ti;
  	document.head.appendChild(et);
}


function init_pageContent(uhv){
  init_bookshelf();
  //var ebd=document.createElement('div');
  var e = document.getElementById('bookshelfContainer');
  var ebd=document.getElementById('bookshelfDiv');
  var ecd=document.createElement('div');
  var ecds=document.createElement('style');

  append_tagsButton(uhv,ebd,tags,tagsChinese); 

  ecd.id='contentDiv';
  //document.body.appendChild(ebd);
  ecds.innerHTML="#contentDiv{margin-top:5%;}";
  e.appendChild(ecd)
  //document.body.appendChild(ecd);
  document.head.appendChild(ecds);
  init_footTools();
  init_search();
}




function append_tagsButton(uhv,e,tags,tagsChinese){
	for(let tagi in tags){
    	var ebd=document.createElement('button');
    	var ebdspan=document.createElement('span');      
        ebdspan.innerHTML=tagsChinese[tagi];     
        if (tags[tagi]==="all"){ 
            ebd.setAttribute('onclick',"show_bookShelf('"+uhv+"')");
        }
        else{
            ebd.setAttribute('onclick',"view_bookShelfWithTag('"+uhv+"','"+tags[tagi]+"')");
        }
      	ebd.appendChild(ebdspan);
        //e.appendChild(ebd);
    }
}

function append_tagCurrentButton(uhv,e,tag,tags,tagsChinese){
    	var ebd=document.createElement('button');
    	var ebdspan=document.createElement('span');      
        ebdspan.innerHTML=tagsChinese[tags.indexOf(tag)];     
        if (tag==="all"){ 
            ebd.setAttribute('onclick',"show_bookShelf('"+uhv+"')");
        }
        else{
            ebd.setAttribute('onclick',"view_bookShelfWithTag('"+uhv+"','"+tag+"')");
        }
      	ebd.appendChild(ebdspan);
        e.appendChild(ebd);
}


function init_footTools(){
  		var e=document.getElementById('toolDivFooter');
  
    	var ebd0=document.createElement('button');
  		ebd0.innerHTML="scrawlZhangYue";
  		ebd0.style.display='block';
  		ebd0.setAttribute("onclick","window.open('/view?vt=page&hv=cod78851c59b3','_blank')");
        e.appendChild(ebd0);
  
    	var ebd1=document.createElement('button');
  		ebd1.innerHTML="ZYsearch";
  		ebd1.style.display='block';
  		ebd1.setAttribute("onclick","window.open('https://www.ireader.com.cn/index.php?ca=search.index&keyword=林谷芳','_blank')");
        e.appendChild(ebd1);  
}

function show_bookShelf(uhv){
var burl="http://127.0.0.1:8088/proxy?p=read&ac=getBookshelf&hv="+uhv+"&bhv=boo4f36c7fe3f&mo=book";
$.getJSON(burl,function(d){
	let e=document.getElementById('contentDiv');
  	e.innerHTML='';
  	let eta=document.createElement("table");
  	let eth=document.createElement("thead");   
  	let etb=document.createElement("tbody");  
  
  	e.className="table-responsive";
  	eta.className="table table-striped table-sm";
  
    let etr=document.createElement("tr");
 	let etd0=document.createElement("td");
  	let etd1=document.createElement("td"); 
    let etd2=document.createElement("td"); 
    let etd3=document.createElement("td");   
  	etd0.innerHTML="book title";
  	etd1.innerHTML="read times";
<<<<<<< HEAD
  	etd2.innerHTML="Know";
  	etd3.innerHTML="delete";  
  	etr.appendChild(etd0);
  	//etr.appendChild(etd1);
  	//etr.appendChild(etd2);
=======
  	etd2.innerHTML="<span style=\"color:blue\">笔记</span>";
  	etd3.innerHTML="delete";  
  	etr.appendChild(etd0);
  	//etr.appendChild(etd1);
  	etr.appendChild(etd2);
>>>>>>> 936d9fdd17824cc34b798b9d092df53c968a8a5e
  	//etr.appendChild(etd3);  
  	eth.appendChild(etr);
  
  
  	for(let bi in d){
      	let bij=JSON.parse(d[bi]);  
        let etr=document.createElement("tr");
      	let etd0=document.createElement("td");
      	let etd1=document.createElement("td");
      	let etd2=document.createElement("td");
      	let etd3=document.createElement("td");      
      	try{
          let bijs=JSON.parse(bij[3]);
          etd0.innerHTML=bijs["label"][0];
        }
      	catch{etd0.innerHTML=d[bi];}
        etd0.setAttribute("onclick","open_book('"+uhv+"','"+bij[0]+"','"+bij[1]+"')");
    	etr.appendChild(etd0);
      	
      	etd1.innerHTML=sum_bookTimes(bij[4],bij[5]);
      	//etr.appendChild(etd1);
      
<<<<<<< HEAD
      	etd2.innerHTML="Know";
      	etd2.setAttribute("onclick","view_knowledge('"+bij[1]+"')");
      	//etr.appendChild(etd2);
=======
      	etd2.innerHTML="<span style=\"color:blue\">note</span>";
      	etd2.setAttribute("onclick","view_knowledge('"+bij[1]+"')");
      	etr.appendChild(etd2);
>>>>>>> 936d9fdd17824cc34b798b9d092df53c968a8a5e
      
      	etd3.innerHTML="delete";
      	etd3.setAttribute('onclick',"delete_book('"+uhv+"','"+bij[0]+"','"+bij[1]+"')");
      	//etr.appendChild(etd3); 
      
      	etb.appendChild(etr);      
      
    }
  	eta.appendChild(eth);
  	eta.appendChild(etb);
  	e.appendChild(eta);
  	//document.body.appendChild(e);
});
}

    function show_bookShelfWithTag(uhv,tag){
var burl="/proxy?p=read&ac=getBookShelfWithTag&uhv="+uhv+"&tag="+tag;
$.getJSON(burl,function(d){
	let e=document.getElementById('contentDiv');
  	e.innerHTML='';
  	let eta=document.createElement("table");
  	let eth=document.createElement("thead");   
  	let etb=document.createElement("tbody");  
  
  	e.className="table-responsive";
  	eta.className="table table-striped table-sm";
  
    let etr=document.createElement("tr");
 	let etd0=document.createElement("td");
  	//let etd1=document.createElement("td"); 
    let etd2=document.createElement("td"); 
  	etd0.innerHTML="book title";
  	//etd1.innerHTML="read times";
  	etd2.innerHTML="Know";
  	etr.appendChild(etd0);
  	//etr.appendChild(etd1);
  	etr.appendChild(etd2);
  	eth.appendChild(etr);
  
  
  	for(let bi in d){
      	let bij=JSON.parse(d[bi]);  
        let etr=document.createElement("tr");
      	let etd0=document.createElement("td");
      	let etd1=document.createElement("td");
      	let etd2=document.createElement("td");
      	//console.log(JSON.parse(Object.values(bij)[0])["label"]);
      	try{
          let bijs=JSON.parse(Object.values(bij)[0]);
          etd0.innerHTML=bijs["label"][0];
        }
      	catch{etd0.innerHTML=d[bi];}
      	let mohv=JSON.parse(Object.keys(bij)[0]);
        etd0.setAttribute("onclick","open_book('"+uhv+"','"+mohv[0]+"','"+mohv[1]+"')");
    	etr.appendChild(etd0);
      	
      	//etd1.innerHTML=sum_bookTimes(bij[4],bij[5]);
      	//etr.appendChild(etd1);
      
      	etd2.innerHTML="Know";
      	etd2.setAttribute("onclick","view_knowledge('"+mohv[1]+"')");
      	etr.appendChild(etd2);
      	etb.appendChild(etr);      
      
    }
  	eta.appendChild(eth);
  	eta.appendChild(etb);
  	e.appendChild(eta);
  	//document.body.appendChild(e);
});

}


function open_book(uhv,mo,hv){
	window.open("http://127.0.0.1:8088/view?vt=page&hv=codd14b46f1a9&uhv="+uhv+"&mo="+mo+"&cid="+hv);
}

function view_bookShelfWithTag(uhv,la){
	window.open("/view?vt=page&hv=cod4ecdf8488d&uhv="+uhv+"&la="+la,"_self");
}

function delete_book(uhv,mo,hv){
	window.open("/proxy?p=read&ac=deleteBook&hv="+uhv+"&mo="+mo+"&bhv="+hv);
}

function sum_bookTimes(lb,lc){
  	let li=parseInt(lb);
  	let lcj=JSON.parse(lc);
	for(let i in lcj){
    	li=li+parseInt(lcj[i]);
    }
  	return li;
}

function view_knowledge(bhv){
<<<<<<< HEAD
	window.open("/view?vt=page&hv=codd360b3579c&bhv="+bhv)
=======
	window.open("http://127.0.0.1:8088/view?vt=page&hv=codd360b3579c&bhv="+bhv)
>>>>>>> 936d9fdd17824cc34b798b9d092df53c968a8a5e
}
//var catalogUrl="/get?gt=model&id=null&mo="+mo+"&tag=title&tp=article&hv="+thv;

	function show_catalog(){
    	try{var e=document.getElementById("bookCatalog");if(e.style.display==="none"){e.style.display="block"}else{e.style.display="none";}}
        catch{pop_catalog();}
    }

	function pop_catalog(){
      	  var bce=document.createElement("div");
      	  bce.id="bookCatalog";
          $.getJSON(catalogUrl,function(d){
          var oe=document.createElement("ol");
          for (let ki in d){
              let e=document.createElement("li");
              e.innerHTML=d[ki];
              e.setAttribute("onclick","view_article("+ki+")");
			  oe.appendChild(e);
          }
          insert_CSS("#bookCatalog{position:fixed;top:5%;height:85%;width:90%;left:5%;background-color:#FAF9DE;overflow:auto;}#bookCatalog>ol>li{text-align:center;border:0.1px solid #f2f2f2;background-color:#CCE8CF;padding:5px 5px;}#bookCatalog>ol>li:hover{background-color:#f2f2f2;color:red;}");
          bce.appendChild(oe);
      });
    	  document.body.appendChild(bce);
    }

    function view_article(i){
      window.open("/view?vt=page&hv=123554b514bb4&tp=article&tag=text&mo="+mo+"&id="+i+"&thv="+thv);
    }

function init_bookshelf(){
	var ev=document.createElement("div");
	var evc=document.createElement("div");  
	var evs=document.createElement("style");  
  	ev.id="bookshelfDiv";
  	evc.id="bookshelfCurrentDiv";
  	ev.appendChild(evc);
  	document.body.appendChild(ev);
  	evs.innerHTML="#bookshelfDiv>button{display:none}#bookshelfDiv>button{max-width:0.2em;font-size:0.1em;min-height:0.3em;}#bookshelfDiv{top:0;left:0;position:fixed;max-width:10%;min-width:3%;max-height:8%;min-height:2%;display:flex;flex-wrap:wrap;transition:width .2s ease,background-color .3s ease,max-width .7s ease,left .5s ease;}#bookshelfDiv:hover{border:1px red solid;top:0;left:1%;position:fixed;background-color:rgb(179 70 9);max-width:70%;min-width:30%;max-height:50%;min-height:20%;display:flex;flex-wrap:wrap;}#bookshelfDiv:hover>button{max-width:2em;font-size:1em;}#bookshelfDiv:hover>button{display:inline}";
  	document.head.appendChild(evs);
  
}
function init_search(){
	var ev=document.createElement("div");
	var evidiv=document.createElement("div");
	var evi=document.createElement("input");
	var evspandiv=document.createElement("div");  
	var evspan=document.createElement("span");
  	ev.id="searchDiv";
  	evidiv.id="searchInputDiv";
  	evspandiv.id="searchSpanDiv";  
  	evi.id="searchInput";  
  	evspan.innerHTML="书目";
  	evspandiv.setAttribute("onclick","search();");
  	evidiv.appendChild(evi);
  	ev.appendChild(evidiv);
  	evspandiv.appendChild(evspan);
  	ev.appendChild(evspandiv);  
  	document.body.appendChild(ev);
  	append_style("#searchInputDiv{display:none;width:6em}#searchDiv{border:1px red solid;top:2%;right:5%;position:fixed;width:1.2em;font-size:1em;background-color:#ef8787;transition:width .2s ease,padding .5s ease;}#searchSpanDiv{color:#f3f3f3;text-align:center;}#searchDiv:hover>#searchInputDiv{display:inline;width:100%;}#searchDiv:hover{width:12em}#searchDiv>#searchSpanDiv:hover{color:#264765;width:100%;}");
  
}


function search(){
	let ei=document.getElementById("searchInput");
	if(ei.value.length>0){
      	show_bookShelfWithSearch(ei.value);
  		ei.value="";
    }
}


function append_style(s){
	var evs=document.createElement("style");  
  	evs.innerHTML=s;
  	document.head.appendChild(evs);
}

function show_bookShelfWithSearch(se){
var burl="/proxy?p=read&ac=search&uhv=1236c7672f3cb&se="+se;
$.getJSON(burl,function(d){
	let e=document.getElementById('contentDiv');
  	e.innerHTML='';
  	let eta=document.createElement("table");
  	let eth=document.createElement("thead");   
  	let etb=document.createElement("tbody");  
  
  	e.className="table-responsive";
  	eta.className="table table-striped table-sm";
  
    let etr=document.createElement("tr");
 	let etd0=document.createElement("td");
  	let etd1=document.createElement("td"); 
    let etd2=document.createElement("td"); 
    let etd3=document.createElement("td");   
  	etd0.innerHTML="book title";
  	etd1.innerHTML="read times";
  	etd2.innerHTML="Know";
  	etd3.innerHTML="delete";  
  	etr.appendChild(etd0);
  	etr.appendChild(etd1);
  	etr.appendChild(etd2);
  	etr.appendChild(etd3);  
  	eth.appendChild(etr);
  
  
  	for(let bi in d){
      	let bij=JSON.parse(d[bi]);  
        let etr=document.createElement("tr");
      	let etd0=document.createElement("td");
      	let etd1=document.createElement("td");
      	let etd2=document.createElement("td");
      	let etd3=document.createElement("td");      
      	try{
          let bijs=JSON.parse(bij[3]);
          etd0.innerHTML=bijs["label"][0];
        }
      	catch{etd0.innerHTML=d[bi];}
        etd0.setAttribute("onclick","open_book('"+bij[0]+"','"+bij[1]+"')");
    	etr.appendChild(etd0);
      	
      	etd1.innerHTML=sum_bookTimes(bij[4],bij[5]);
      	etr.appendChild(etd1);
      
      	etd2.innerHTML="Know";
      	etr.appendChild(etd2);
      
      	etd3.innerHTML="delete";
      	etd3.setAttribute('onclick',"delete_book('"+bij[0]+"','"+bij[1]+"')");
      	etr.appendChild(etd3); 
      
      	etb.appendChild(etr);      
      
    }
  	eta.appendChild(eth);
  	eta.appendChild(etb);
  	e.appendChild(eta);
  	//document.body.appendChild(e);
})}