var _JUPYTERLAB;(()=>{"use strict";var e,r,t,n,o,a,i,l,u,d,f,s,p,c,h,v,b,y,g,m,w={611:(e,r,t)=>{var n={"./index":()=>Promise.all([t.e(478),t.e(879),t.e(211),t.e(657)]).then((()=>()=>t(879))),"./extension":()=>Promise.all([t.e(211),t.e(133)]).then((()=>()=>t(133))),"./mimeExtension":()=>t.e(423).then((()=>()=>t(423)))},o=(e,r)=>(t.R=r,r=t.o(n,e)?n[e]():Promise.resolve().then((()=>{throw new Error('Module "'+e+'" does not exist in container.')})),t.R=void 0,r),a=(e,r)=>{if(t.S){var n=t.S.default,o="default";if(n&&n!==e)throw new Error("Container initialization failed as it has already been initialized with a different share scope");return t.S[o]=e,t.I(o,r)}};t.d(r,{get:()=>o,init:()=>a})}},j={};function P(e){var r=j[e];if(void 0!==r)return r.exports;var t=j[e]={id:e,loaded:!1,exports:{}};return w[e].call(t.exports,t,t.exports,P),t.loaded=!0,t.exports}P.m=w,P.c=j,P.n=e=>{var r=e&&e.__esModule?()=>e.default:()=>e;return P.d(r,{a:r}),r},r=Object.getPrototypeOf?e=>Object.getPrototypeOf(e):e=>e.__proto__,P.t=function(t,n){if(1&n&&(t=this(t)),8&n)return t;if("object"==typeof t&&t){if(4&n&&t.__esModule)return t;if(16&n&&"function"==typeof t.then)return t}var o=Object.create(null);P.r(o);var a={};e=e||[null,r({}),r([]),r(r)];for(var i=2&n&&t;"object"==typeof i&&!~e.indexOf(i);i=r(i))Object.getOwnPropertyNames(i).forEach((e=>a[e]=()=>t[e]));return a.default=()=>t,P.d(o,a),o},P.d=(e,r)=>{for(var t in r)P.o(r,t)&&!P.o(e,t)&&Object.defineProperty(e,t,{enumerable:!0,get:r[t]})},P.f={},P.e=e=>Promise.all(Object.keys(P.f).reduce(((r,t)=>(P.f[t](e,r),r)),[])),P.u=e=>e+"."+{133:"fa90072794e24ddca3af",211:"891e9043bb1ebd1a1607",423:"5c5d1f420114d7d75b9b",478:"07d8d9ae56ba83491686",486:"52aa9063b291ec574154",657:"17023484aff5cb288d0d",879:"b55d82ff9b3516e96fb0"}[e]+".js?v="+{133:"fa90072794e24ddca3af",211:"891e9043bb1ebd1a1607",423:"5c5d1f420114d7d75b9b",478:"07d8d9ae56ba83491686",486:"52aa9063b291ec574154",657:"17023484aff5cb288d0d",879:"b55d82ff9b3516e96fb0"}[e],P.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),P.o=(e,r)=>Object.prototype.hasOwnProperty.call(e,r),t={},n="jupyterlab-plotly:",P.l=(e,r,o,a)=>{if(t[e])t[e].push(r);else{var i,l;if(void 0!==o)for(var u=document.getElementsByTagName("script"),d=0;d<u.length;d++){var f=u[d];if(f.getAttribute("src")==e||f.getAttribute("data-webpack")==n+o){i=f;break}}i||(l=!0,(i=document.createElement("script")).charset="utf-8",i.timeout=120,P.nc&&i.setAttribute("nonce",P.nc),i.setAttribute("data-webpack",n+o),i.src=e),t[e]=[r];var s=(r,n)=>{i.onerror=i.onload=null,clearTimeout(p);var o=t[e];if(delete t[e],i.parentNode&&i.parentNode.removeChild(i),o&&o.forEach((e=>e(n))),r)return r(n)},p=setTimeout(s.bind(null,void 0,{type:"timeout",target:i}),12e4);i.onerror=s.bind(null,i.onerror),i.onload=s.bind(null,i.onload),l&&document.head.appendChild(i)}},P.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},P.nmd=e=>(e.paths=[],e.children||(e.children=[]),e),(()=>{P.S={};var e={},r={};P.I=(t,n)=>{n||(n=[]);var o=r[t];if(o||(o=r[t]={}),!(n.indexOf(o)>=0)){if(n.push(o),e[t])return e[t];P.o(P.S,t)||(P.S[t]={});var a=P.S[t],i="jupyterlab-plotly",l=(e,r,t,n)=>{var o=a[e]=a[e]||{},l=o[r];(!l||!l.loaded&&(!n!=!l.eager?n:i>l.from))&&(o[r]={get:t,from:i,eager:!!n})},u=[];switch(t){case"default":l("jupyterlab-plotly","5.0.0-rc.2",(()=>Promise.all([P.e(478),P.e(879),P.e(211),P.e(657)]).then((()=>()=>P(879))))),l("lodash","4.17.21",(()=>P.e(486).then((()=>()=>P(486)))))}return e[t]=u.length?Promise.all(u).then((()=>e[t]=1)):1}}})(),(()=>{var e;P.g.importScripts&&(e=P.g.location+"");var r=P.g.document;if(!e&&r&&(r.currentScript&&(e=r.currentScript.src),!e)){var t=r.getElementsByTagName("script");t.length&&(e=t[t.length-1].src)}if(!e)throw new Error("Automatic publicPath is not supported in this browser");e=e.replace(/#.*$/,"").replace(/\?.*$/,"").replace(/\/[^\/]+$/,"/"),P.p=e})(),o=e=>{var r=e=>e.split(".").map((e=>+e==e?+e:e)),t=/^([^-+]+)?(?:-([^+]+))?(?:\+(.+))?$/.exec(e),n=t[1]?r(t[1]):[];return t[2]&&(n.length++,n.push.apply(n,r(t[2]))),t[3]&&(n.push([]),n.push.apply(n,r(t[3]))),n},a=(e,r)=>{e=o(e),r=o(r);for(var t=0;;){if(t>=e.length)return t<r.length&&"u"!=(typeof r[t])[0];var n=e[t],a=(typeof n)[0];if(t>=r.length)return"u"==a;var i=r[t],l=(typeof i)[0];if(a!=l)return"o"==a&&"n"==l||"s"==l||"u"==a;if("o"!=a&&"u"!=a&&n!=i)return n<i;t++}},i=e=>{var r=e[0],t="";if(1===e.length)return"*";if(r+.5){t+=0==r?">=":-1==r?"<":1==r?"^":2==r?"~":r>0?"=":"!=";for(var n=1,o=1;o<e.length;o++)n--,t+="u"==(typeof(l=e[o]))[0]?"-":(n>0?".":"")+(n=2,l);return t}var a=[];for(o=1;o<e.length;o++){var l=e[o];a.push(0===l?"not("+u()+")":1===l?"("+u()+" || "+u()+")":2===l?a.pop()+" "+a.pop():i(l))}return u();function u(){return a.pop().replace(/^\((.+)\)$/,"$1")}},l=(e,r)=>{if(0 in e){r=o(r);var t=e[0],n=t<0;n&&(t=-t-1);for(var a=0,i=1,u=!0;;i++,a++){var d,f,s=i<e.length?(typeof e[i])[0]:"";if(a>=r.length||"o"==(f=(typeof(d=r[a]))[0]))return!u||("u"==s?i>t&&!n:""==s!=n);if("u"==f){if(!u||"u"!=s)return!1}else if(u)if(s==f)if(i<=t){if(d!=e[i])return!1}else{if(n?d>e[i]:d<e[i])return!1;d!=e[i]&&(u=!1)}else if("s"!=s&&"n"!=s){if(n||i<=t)return!1;u=!1,i--}else{if(i<=t||f<s!=n)return!1;u=!1}else"s"!=s&&"n"!=s&&(u=!1,i--)}}var p=[],c=p.pop.bind(p);for(a=1;a<e.length;a++){var h=e[a];p.push(1==h?c()|c():2==h?c()&c():h?l(h,r):!c())}return!!c()},u=(e,r)=>{var t=P.S[e];if(!t||!P.o(t,r))throw new Error("Shared module "+r+" doesn't exist in shared scope "+e);return t},d=(e,r)=>{var t=e[r];return Object.keys(t).reduce(((e,r)=>!e||!t[e].loaded&&a(e,r)?r:e),0)},f=(e,r,t)=>"Unsatisfied version "+r+" of shared singleton module "+e+" (required "+i(t)+")",s=(e,r,t,n)=>{var o=d(e,t);return l(n,o)||"undefined"!=typeof console&&console.warn&&console.warn(f(t,o,n)),c(e[t][o])},p=(e,r,t)=>{var n=e[r];return(r=Object.keys(n).reduce(((e,r)=>!l(t,r)||e&&!a(e,r)?e:r),0))&&n[r]},c=e=>(e.loaded=1,e.get()),v=(h=e=>function(r,t,n,o){var a=P.I(r);return a&&a.then?a.then(e.bind(e,r,P.S[r],t,n,o)):e(r,P.S[r],t,n,o)})(((e,r,t,n)=>(u(e,t),s(r,0,t,n)))),b=h(((e,r,t,n,o)=>{var a=r&&P.o(r,t)&&p(r,t,n);return a?c(a):o()})),y={},g={431:()=>b("default","lodash",[1,4,17,4],(()=>P.e(486).then((()=>()=>P(486))))),211:()=>v("default","@jupyter-widgets/base",[,[1,4,0,0],[1,3,0,0],[1,2,0,0],1,1]),510:()=>v("default","@lumino/widgets",[1,1,16,1])},m={211:[211],423:[510],879:[431]},P.f.consumes=(e,r)=>{P.o(m,e)&&m[e].forEach((e=>{if(P.o(y,e))return r.push(y[e]);var t=r=>{y[e]=0,P.m[e]=t=>{delete P.c[e],t.exports=r()}},n=r=>{delete y[e],P.m[e]=t=>{throw delete P.c[e],r}};try{var o=g[e]();o.then?r.push(y[e]=o.then(t).catch(n)):t(o)}catch(e){n(e)}}))},(()=>{var e={860:0};P.f.j=(r,t)=>{var n=P.o(e,r)?e[r]:void 0;if(0!==n)if(n)t.push(n[2]);else if(211!=r){var o=new Promise(((t,o)=>n=e[r]=[t,o]));t.push(n[2]=o);var a=P.p+P.u(r),i=new Error;P.l(a,(t=>{if(P.o(e,r)&&(0!==(n=e[r])&&(e[r]=void 0),n)){var o=t&&("load"===t.type?"missing":t.type),a=t&&t.target&&t.target.src;i.message="Loading chunk "+r+" failed.\n("+o+": "+a+")",i.name="ChunkLoadError",i.type=o,i.request=a,n[1](i)}}),"chunk-"+r,r)}else e[r]=0};var r=(r,t)=>{var n,o,[a,i,l]=t,u=0;for(n in i)P.o(i,n)&&(P.m[n]=i[n]);for(l&&l(P),r&&r(t);u<a.length;u++)o=a[u],P.o(e,o)&&e[o]&&e[o][0](),e[a[u]]=0},t=self.webpackChunkjupyterlab_plotly=self.webpackChunkjupyterlab_plotly||[];t.forEach(r.bind(null,0)),t.push=r.bind(null,t.push.bind(t))})();var S=P(611);(_JUPYTERLAB=void 0===_JUPYTERLAB?{}:_JUPYTERLAB)["jupyterlab-plotly"]=S})();