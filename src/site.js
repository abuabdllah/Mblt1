(function(){
  var WA = "966564612017";

  // تتبع التحويلات: يشتغل لما تضيف كود جوجل ادز في <head> (gtag) وتحط معرف التحويل هنا
  var CONVERSION = ""; // مثال: "AW-XXXXXXXXX/XXXXXXXXXXXX"
  function track(kind){
    try{
      if (window.gtag){
        if (CONVERSION) window.gtag("event","conversion",{send_to:CONVERSION});
        window.gtag("event","lead_click",{method:kind});
      }
    }catch(e){}
  }
  document.addEventListener("click",function(e){
    var a = e.target.closest && e.target.closest("a");
    if(!a) return;
    var h = a.getAttribute("href")||"";
    if (h.indexOf("tel:")===0) track("call");
    else if (h.indexOf("wa.me")>-1) track("whatsapp");
  });

  // فورم طلب المعاينة → رسالة واتساب جاهزة
  var forms = document.querySelectorAll("form[data-wa]");
  forms.forEach(function(f){
    f.addEventListener("submit",function(e){
      e.preventDefault();
      var g = function(n){ var el=f.querySelector("[name="+n+"]"); return el? el.value.trim() : ""; };
      var name=g("name"), area=g("area"), service=g("service"), msg=g("msg");
      if(!area){ var a=f.querySelector("[name=area]"); a && a.focus(); return; }
      var text = "السلام عليكم، أبغى معاينة تبليط"
        + (name? "\nالاسم: "+name : "")
        + "\nالحي/المدينة: "+area
        + (service? "\nالخدمة: "+service : "")
        + (msg? "\nالتفاصيل: "+msg : "")
        + "\n(من موقع mblt1.com)";
      var url = "https://wa.me/"+WA+"?text="+encodeURIComponent(text);
      track("form");
      var fb = f.querySelector(".fallback");
      if (fb){ fb.hidden=false; var l=fb.querySelector("a"); if(l) l.href=url; }
      window.location.href = url;
    });
  });

  // حاسبة البلاط
  var c = document.getElementById("calc");
  if (c){
    var $ = function(id){ return document.getElementById(id); };
    function n(id){ var v=parseFloat(($(id).value||"").replace(",",".")); return isNaN(v)?0:v; }
    function fmt(x,d){ return x.toLocaleString("ar-SA",{maximumFractionDigits:d||0}); }
    function run(){
      var area = n("c-area");
      if (!area){ area = n("c-len")*n("c-wid"); }
      var size = $("c-size").value.split("x");
      var tw=parseFloat(size[0])/100, th=parseFloat(size[1])/100;
      var waste = parseFloat($("c-pattern").value);
      var box = n("c-box");
      var need = area*(1+waste);
      var tileArea = tw*th;
      var tiles = tileArea? Math.ceil(need/tileArea) : 0;
      var boxes = box? Math.ceil(need/box) : 0;
      var glue = Math.ceil(area*(tileArea>=0.36?6:5)/20); // كيس 20 كجم تقريبًا
      $("o-area").textContent = fmt(area,1)+" م²";
      $("o-need").textContent = fmt(need,1)+" م²";
      $("o-tiles").textContent = fmt(tiles)+" بلاطة";
      $("o-boxes").textContent = box? fmt(boxes)+" كرتون" : "حدد مساحة الكرتون";
      $("o-glue").textContent = area? "≈ "+fmt(glue)+" كيس" : "—";
    }
    c.addEventListener("input",run); run();
  }
})();
