parcelRequire=function(e,r,n,t){function i(n,t){function o(e){return i(o.resolve(e))}function c(r){return e[n][1][r]||r}if(!r[n]){if(!e[n]){var l="function"==typeof parcelRequire&&parcelRequire;if(!t&&l)return l(n,!0);if(u)return u(n,!0);if(f&&"string"==typeof n)return f(n);var p=new Error("Cannot find module '"+n+"'");throw p.code="MODULE_NOT_FOUND",p}o.resolve=c;var a=r[n]=new i.Module(n);e[n][0].call(a.exports,o,a,a.exports,this)}return r[n].exports}function o(e){this.id=e,this.bundle=i,this.exports={}}var u="function"==typeof parcelRequire&&parcelRequire,f="function"==typeof require&&require;i.isParcelRequire=!0,i.Module=o,i.modules=e,i.cache=r,i.parent=u;for(var c=0;c<n.length;c++)i(n[c]);if(n.length){var l=i(n[n.length-1]);"object"==typeof exports&&"undefined"!=typeof module?module.exports=l:"function"==typeof define&&define.amd?define(function(){return l}):t&&(this[t]=l)}return i}({5:[function(require,module,exports) {
"use strict";function e(){}Object.defineProperty(exports,"__esModule",{value:!0});var t={},n=[],o=[];function r(r,i){var l,a,p,s,c=o;for(s=arguments.length;s-- >2;)n.push(arguments[s]);for(i&&null!=i.children&&(n.length||n.push(i.children),delete i.children);n.length;)if((a=n.pop())&&void 0!==a.pop)for(s=a.length;s--;)n.push(a[s]);else"boolean"==typeof a&&(a=null),(p="function"!=typeof r)&&(null==a?a="":"number"==typeof a?a=String(a):"string"!=typeof a&&(p=!1)),p&&l?c[c.length-1]+=a:c===o?c=[a]:c.push(a),l=p;var u=new e;return u.nodeName=r,u.children=c,u.attributes=null==i?void 0:i,u.key=null==i?void 0:i.key,void 0!==t.vnode&&t.vnode(u),u}function i(e,t){for(var n in t)e[n]=t[n];return e}var l="function"==typeof Promise?Promise.resolve().then.bind(Promise.resolve()):setTimeout;function a(e,t){return r(e.nodeName,i(i({},e.attributes),t),arguments.length>2?[].slice.call(arguments,2):e.children)}var p=/acit|ex(?:s|g|n|p|$)|rph|ows|mnc|ntw|ine[ch]|zoo|^ord/i,s=[];function c(e){!e._dirty&&(e._dirty=!0)&&1==s.push(e)&&(t.debounceRendering||l)(u)}function u(){var e,t=s;for(s=[];e=t.pop();)e._dirty&&A(e)}function f(e,t,n){return"string"==typeof t||"number"==typeof t?void 0!==e.splitText:"string"==typeof t.nodeName?!e._componentConstructor&&d(e,t.nodeName):n||e._componentConstructor===t.nodeName}function d(e,t){return e.normalizedNodeName===t||e.nodeName.toLowerCase()===t.toLowerCase()}function _(e){var t=i({},e.attributes);t.children=e.children;var n=e.nodeName.defaultProps;if(void 0!==n)for(var o in n)void 0===t[o]&&(t[o]=n[o]);return t}function v(e,t){var n=t?document.createElementNS("http://www.w3.org/2000/svg",e):document.createElement(e);return n.normalizedNodeName=e,n}function m(e){var t=e.parentNode;t&&t.removeChild(e)}function h(e,t,n,o,r){if("className"===t&&(t="class"),"key"===t);else if("ref"===t)n&&n(null),o&&o(e);else if("class"!==t||r)if("style"===t){if(o&&"string"!=typeof o&&"string"!=typeof n||(e.style.cssText=o||""),o&&"object"==typeof o){if("string"!=typeof n)for(var i in n)i in o||(e.style[i]="");for(var i in o)e.style[i]="number"==typeof o[i]&&!1===p.test(i)?o[i]+"px":o[i]}}else if("dangerouslySetInnerHTML"===t)o&&(e.innerHTML=o.__html||"");else if("o"==t[0]&&"n"==t[1]){var l=t!==(t=t.replace(/Capture$/,""));t=t.toLowerCase().substring(2),o?n||e.addEventListener(t,y,l):e.removeEventListener(t,y,l),(e._listeners||(e._listeners={}))[t]=o}else if("list"!==t&&"type"!==t&&!r&&t in e)b(e,t,null==o?"":o),null!=o&&!1!==o||e.removeAttribute(t);else{var a=r&&t!==(t=t.replace(/^xlink\:?/,""));null==o||!1===o?a?e.removeAttributeNS("http://www.w3.org/1999/xlink",t.toLowerCase()):e.removeAttribute(t):"function"!=typeof o&&(a?e.setAttributeNS("http://www.w3.org/1999/xlink",t.toLowerCase(),o):e.setAttribute(t,o))}else e.className=o||""}function b(e,t,n){try{e[t]=n}catch(e){}}function y(e){return this._listeners[e.type](t.event&&t.event(e)||e)}var x=[],C=0,g=!1,N=!1;function k(){for(var e;e=x.pop();)t.afterMount&&t.afterMount(e),e.componentDidMount&&e.componentDidMount()}function w(e,t,n,o,r,i){C++||(g=null!=r&&void 0!==r.ownerSVGElement,N=null!=e&&!("__preactattr_"in e));var l=S(e,t,n,o,i);return r&&l.parentNode!==r&&r.appendChild(l),--C||(N=!1,i||k()),l}function S(e,t,n,o,r){var i=e,l=g;if(null!=t&&"boolean"!=typeof t||(t=""),"string"==typeof t||"number"==typeof t)return e&&void 0!==e.splitText&&e.parentNode&&(!e._component||r)?e.nodeValue!=t&&(e.nodeValue=t):(i=document.createTextNode(t),e&&(e.parentNode&&e.parentNode.replaceChild(i,e),L(e,!0))),i.__preactattr_=!0,i;var a=t.nodeName;if("function"==typeof a)return D(e,t,n,o);if(g="svg"===a||"foreignObject"!==a&&g,a=String(a),(!e||!d(e,a))&&(i=v(a,g),e)){for(;e.firstChild;)i.appendChild(e.firstChild);e.parentNode&&e.parentNode.replaceChild(i,e),L(e,!0)}var p=i.firstChild,s=i.__preactattr_,c=t.children;if(null==s){s=i.__preactattr_={};for(var u=i.attributes,f=u.length;f--;)s[u[f].name]=u[f].value}return!N&&c&&1===c.length&&"string"==typeof c[0]&&null!=p&&void 0!==p.splitText&&null==p.nextSibling?p.nodeValue!=c[0]&&(p.nodeValue=c[0]):(c&&c.length||null!=p)&&U(i,c,n,o,N||null!=s.dangerouslySetInnerHTML),P(i,t.attributes,s),g=l,i}function U(e,t,n,o,r){var i,l,a,p,s,c=e.childNodes,u=[],d={},_=0,v=0,h=c.length,b=0,y=t?t.length:0;if(0!==h)for(var x=0;x<h;x++){var C=c[x],g=C.__preactattr_;null!=(N=y&&g?C._component?C._component.__key:g.key:null)?(_++,d[N]=C):(g||(void 0!==C.splitText?!r||C.nodeValue.trim():r))&&(u[b++]=C)}if(0!==y)for(x=0;x<y;x++){var N;if(s=null,null!=(N=(p=t[x]).key))_&&void 0!==d[N]&&(s=d[N],d[N]=void 0,_--);else if(!s&&v<b)for(i=v;i<b;i++)if(void 0!==u[i]&&f(l=u[i],p,r)){s=l,u[i]=void 0,i===b-1&&b--,i===v&&v++;break}s=S(s,p,n,o),a=c[x],s&&s!==e&&s!==a&&(null==a?e.appendChild(s):s===a.nextSibling?m(a):e.insertBefore(s,a))}if(_)for(var x in d)void 0!==d[x]&&L(d[x],!1);for(;v<=b;)void 0!==(s=u[b--])&&L(s,!1)}function L(e,t){var n=e._component;n?H(n):(null!=e.__preactattr_&&e.__preactattr_.ref&&e.__preactattr_.ref(null),!1!==t&&null!=e.__preactattr_||m(e),M(e))}function M(e){for(e=e.lastChild;e;){var t=e.previousSibling;L(e,!0),e=t}}function P(e,t,n){var o;for(o in n)t&&null!=t[o]||null==n[o]||h(e,o,n[o],n[o]=void 0,g);for(o in t)"children"===o||"innerHTML"===o||o in n&&t[o]===("value"===o||"checked"===o?e[o]:n[o])||h(e,o,n[o],n[o]=t[o],g)}var T={};function B(e){var t=e.constructor.name;(T[t]||(T[t]=[])).push(e)}function E(e,t,n){var o,r=T[e.name];if(e.prototype&&e.prototype.render?(o=new e(t,n),j.call(o,t,n)):((o=new j(t,n)).constructor=e,o.render=W),r)for(var i=r.length;i--;)if(r[i].constructor===e){o.nextBase=r[i].nextBase,r.splice(i,1);break}return o}function W(e,t,n){return this.constructor(e,n)}function V(e,n,o,r,i){e._disable||(e._disable=!0,(e.__ref=n.ref)&&delete n.ref,(e.__key=n.key)&&delete n.key,!e.base||i?e.componentWillMount&&e.componentWillMount():e.componentWillReceiveProps&&e.componentWillReceiveProps(n,r),r&&r!==e.context&&(e.prevContext||(e.prevContext=e.context),e.context=r),e.prevProps||(e.prevProps=e.props),e.props=n,e._disable=!1,0!==o&&(1!==o&&!1===t.syncComponentUpdates&&e.base?c(e):A(e,1,i)),e.__ref&&e.__ref(e))}function A(e,n,o,r){if(!e._disable){var l,a,p,s=e.props,c=e.state,u=e.context,f=e.prevProps||s,d=e.prevState||c,v=e.prevContext||u,m=e.base,h=e.nextBase,b=m||h,y=e._component,g=!1;if(m&&(e.props=f,e.state=d,e.context=v,2!==n&&e.shouldComponentUpdate&&!1===e.shouldComponentUpdate(s,c,u)?g=!0:e.componentWillUpdate&&e.componentWillUpdate(s,c,u),e.props=s,e.state=c,e.context=u),e.prevProps=e.prevState=e.prevContext=e.nextBase=null,e._dirty=!1,!g){l=e.render(s,c,u),e.getChildContext&&(u=i(i({},u),e.getChildContext()));var N,S,U=l&&l.nodeName;if("function"==typeof U){var M=_(l);(a=y)&&a.constructor===U&&M.key==a.__key?V(a,M,1,u,!1):(N=a,e._component=a=E(U,M,u),a.nextBase=a.nextBase||h,a._parentComponent=e,V(a,M,0,u,!1),A(a,1,o,!0)),S=a.base}else p=b,(N=y)&&(p=e._component=null),(b||1===n)&&(p&&(p._component=null),S=w(p,l,u,o||!m,b&&b.parentNode,!0));if(b&&S!==b&&a!==y){var P=b.parentNode;P&&S!==P&&(P.replaceChild(S,b),N||(b._component=null,L(b,!1)))}if(N&&H(N),e.base=S,S&&!r){for(var T=e,B=e;B=B._parentComponent;)(T=B).base=S;S._component=T,S._componentConstructor=T.constructor}}if(!m||o?x.unshift(e):g||(e.componentDidUpdate&&e.componentDidUpdate(f,d,v),t.afterUpdate&&t.afterUpdate(e)),null!=e._renderCallbacks)for(;e._renderCallbacks.length;)e._renderCallbacks.pop().call(e);C||r||k()}}function D(e,t,n,o){for(var r=e&&e._component,i=r,l=e,a=r&&e._componentConstructor===t.nodeName,p=a,s=_(t);r&&!p&&(r=r._parentComponent);)p=r.constructor===t.nodeName;return r&&p&&(!o||r._component)?(V(r,s,3,n,o),e=r.base):(i&&!a&&(H(i),e=l=null),r=E(t.nodeName,s,n),e&&!r.nextBase&&(r.nextBase=e,l=null),V(r,s,1,n,o),e=r.base,l&&e!==l&&(l._component=null,L(l,!1))),e}function H(e){t.beforeUnmount&&t.beforeUnmount(e);var n=e.base;e._disable=!0,e.componentWillUnmount&&e.componentWillUnmount(),e.base=null;var o=e._component;o?H(o):n&&(n.__preactattr_&&n.__preactattr_.ref&&n.__preactattr_.ref(null),e.nextBase=n,m(n),B(e),M(n)),e.__ref&&e.__ref(null)}function j(e,t){this._dirty=!0,this.context=t,this.props=e,this.state=this.state||{}}function z(e,t,n){return w(n,e,{},!1,t,!1)}i(j.prototype,{setState:function(e,t){var n=this.state;this.prevState||(this.prevState=i({},n)),i(n,"function"==typeof e?e(n,this.props):e),t&&(this._renderCallbacks=this._renderCallbacks||[]).push(t),c(this)},forceUpdate:function(e){e&&(this._renderCallbacks=this._renderCallbacks||[]).push(e),A(this,2)},render:function(){}});var R={h:r,createElement:r,cloneElement:a,Component:j,render:z,rerender:u,options:t};exports.h=r,exports.createElement=r,exports.cloneElement=a,exports.Component=j,exports.render=z,exports.rerender=u,exports.options=t,exports.default=R;
},{}],17:[function(require,module,exports) {
var global = arguments[3];
var e=arguments[3];Object.defineProperty(exports,"__esModule",{value:!0});var t={name:"appTime",reducer:Date.now,selectAppTime:function(e){return e.appTime}},r={STARTED:1,FINISHED:-1,FAILED:-1},n=/_(STARTED|FINISHED|FAILED)$/,o={name:"asyncCount",reducer:function(e,t){void 0===e&&(e=0);var o=n.exec(t.type);return o?e+r[o[1]]:e},selectAsyncActive:function(e){return e.asyncCount>0}},a="object"==typeof e&&e&&e.Object===Object&&e,c="object"==typeof self&&self&&self.Object===Object&&self,i=(a||c||Function("return this")()).Symbol,u=Object.prototype,s=u.hasOwnProperty,l=u.toString,f=i?i.toStringTag:void 0,d=Object.prototype.toString,p="[object Null]",h="[object Undefined]",v=i?i.toStringTag:void 0;function y(e){return null==e?void 0===e?h:p:v&&v in Object(e)?function(e){var t=s.call(e,f),r=e[f];try{e[f]=void 0;var n=!0}catch(e){}var o=l.call(e);return n&&(t?e[f]=r:delete e[f]),o}(e):function(e){return d.call(e)}(e)}var g,m,b=(g=Object.getPrototypeOf,m=Object,function(e){return g(m(e))}),E="[object Object]",w=Function.prototype,A=Object.prototype,x=w.toString,T=A.hasOwnProperty,O=x.call(Object);function S(e){if(!function(e){return null!=e&&"object"==typeof e}(e)||y(e)!=E)return!1;var t=b(e);if(null===t)return!0;var r=T.call(t,"constructor")&&t.constructor;return"function"==typeof r&&r instanceof r&&x.call(r)==O}var I=function(t){var r,n=("undefined"!=typeof self?self:"undefined"!=typeof window?window:"undefined"!=typeof e?e:"undefined"!=typeof module?module:Function("return this")()).Symbol;return"function"==typeof n?n.observable?r=n.observable:(r=n("observable"),n.observable=r):r="@@observable",r}(),R={INIT:"@@redux/INIT"};function j(e,t,r){var n;if("function"==typeof t&&void 0===r&&(r=t,t=void 0),void 0!==r){if("function"!=typeof r)throw new Error("Expected the enhancer to be a function.");return r(j)(e,t)}if("function"!=typeof e)throw new Error("Expected the reducer to be a function.");var o=e,a=t,c=[],i=c,u=!1;function s(){i===c&&(i=c.slice())}function l(){return a}function f(e){if("function"!=typeof e)throw new Error("Expected listener to be a function.");var t=!0;return s(),i.push(e),function(){if(t){t=!1,s();var r=i.indexOf(e);i.splice(r,1)}}}function d(e){if(!S(e))throw new Error("Actions must be plain objects. Use custom middleware for async actions.");if(void 0===e.type)throw new Error('Actions may not have an undefined "type" property. Have you misspelled a constant?');if(u)throw new Error("Reducers may not dispatch actions.");try{u=!0,a=o(a,e)}finally{u=!1}for(var t=c=i,r=0;r<t.length;r++)(0,t[r])();return e}return d({type:R.INIT}),(n={dispatch:d,subscribe:f,getState:l,replaceReducer:function(e){if("function"!=typeof e)throw new Error("Expected the nextReducer to be a function.");o=e,d({type:R.INIT})}})[I]=function(){var e,t=f;return(e={subscribe:function(e){if("object"!=typeof e)throw new TypeError("Expected the observer to be an object.");function r(){e.next&&e.next(l())}return r(),{unsubscribe:t(r)}}})[I]=function(){return this},e},n}function C(e){"undefined"!=typeof console&&"function"==typeof console.error&&console.error(e);try{throw new Error(e)}catch(e){}}function D(e,t){var r=t&&t.type;return"Given action "+(r&&'"'+r.toString()+'"'||"an action")+', reducer "'+e+'" returned undefined. To ignore an action, you must explicitly return the previous state. If you want this reducer to hold no value, you can return null instead of undefined.'}function N(e){for(var t=Object.keys(e),r={},n=0;n<t.length;n++){var o=t[n];"function"==typeof e[o]&&(r[o]=e[o])}var a=Object.keys(r),c=void 0;try{!function(e){Object.keys(e).forEach(function(t){var r=e[t];if(void 0===r(void 0,{type:R.INIT}))throw new Error('Reducer "'+t+"\" returned undefined during initialization. If the state passed to the reducer is undefined, you must explicitly return the initial state. The initial state may not be undefined. If you don't want to set a value for this reducer, you can use null instead of undefined.");if(void 0===r(void 0,{type:"@@redux/PROBE_UNKNOWN_ACTION_"+Math.random().toString(36).substring(7).split("").join(".")}))throw new Error('Reducer "'+t+"\" returned undefined when probed with a random type. Don't try to handle "+R.INIT+' or other actions in "redux/*" namespace. They are considered private. Instead, you must return the current state for any unknown actions, unless it is undefined, in which case you must return the initial state, regardless of the action type. The initial state may not be undefined, but can be null.')})}(r)}catch(e){c=e}return function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=arguments[1];if(c)throw c;for(var n=!1,o={},i=0;i<a.length;i++){var u=a[i],s=e[u],l=(0,r[u])(s,t);if(void 0===l){var f=D(u,t);throw new Error(f)}o[u]=l,n=n||l!==s}return n?o:e}}function L(e,t){return function(){return t(e.apply(void 0,arguments))}}function P(e,t){if("function"==typeof e)return L(e,t);if("object"!=typeof e||null===e)throw new Error("bindActionCreators expected an object or a function, instead received "+(null===e?"null":typeof e)+'. Did you write "import ActionCreators from" instead of "import * as ActionCreators from"?');for(var r=Object.keys(e),n={},o=0;o<r.length;o++){var a=r[o],c=e[a];"function"==typeof c&&(n[a]=L(c,t))}return n}function U(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];return 0===t.length?function(e){return e}:1===t.length?t[0]:t.reduce(function(e,t){return function(){return e(t.apply(void 0,arguments))}})}var B=Object.assign||function(e){for(var t=1;t<arguments.length;t++){var r=arguments[t];for(var n in r)Object.prototype.hasOwnProperty.call(r,n)&&(e[n]=r[n])}return e};function F(){for(var e=arguments.length,t=Array(e),r=0;r<e;r++)t[r]=arguments[r];return function(e){return function(r,n,o){var a,c=e(r,n,o),i=c.dispatch,u={getState:c.getState,dispatch:function(e){return i(e)}};return a=t.map(function(e){return e(u)}),i=U.apply(void 0,a)(c.dispatch),B({},c,{dispatch:i})}}}function _(){}function k(e,t){return e===t}function H(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:k,r=null,n=null;return function(){return function(e,t,r){if(null===t||null===r||t.length!==r.length)return!1;for(var n=t.length,o=0;o<n;o++)if(!e(t[o],r[o]))return!1;return!0}(t,r,arguments)||(n=e.apply(null,arguments)),r=arguments,n}}var G=function(e){for(var t=arguments.length,r=Array(t>1?t-1:0),n=1;n<t;n++)r[n-1]=arguments[n];return function(){for(var t=arguments.length,n=Array(t),o=0;o<t;o++)n[o]=arguments[o];var a=0,c=n.pop(),i=function(e){var t=Array.isArray(e[0])?e[0]:e;if(!t.every(function(e){return"function"==typeof e})){var r=t.map(function(e){return typeof e}).join(", ");throw new Error("Selector creators expect all input-selectors to be functions, instead received the following types: ["+r+"]")}return t}(n),u=e.apply(void 0,[function(){return a++,c.apply(null,arguments)}].concat(r)),s=H(function(){for(var e=[],t=i.length,r=0;r<t;r++)e.push(i[r].apply(null,arguments));return u.apply(null,e)});return s.resultFunc=c,s.recomputations=function(){return a},s.resetRecomputations=function(){return a=0},s}}(H),q=function(){for(var e=[],t=arguments.length;t--;)e[t]=arguments[t];var r=e.slice(-1)[0],n=function(e,t){var n=t.map(function(t){return function(e,t){if("string"!=typeof t)return t;var r=e[t];if(!r)throw Error("No selector "+t+" found on the obj.");return r}(e,t)});return n.push(r),G.apply(void 0,n)};return n.deps=e.slice(0,-1),n.resultFunc=r,n},M=function(e){var t=function(t){return t.call&&!t.deps||!e[t].deps},r=!1,n=function(n){var o=e[n];t(n)?r=!0:o.deps=o.deps.map(function(t,o){if(t.call){for(var a in e)if(e[a]===t)return a;if(!t.deps)return r=!0,t}if(e[t])return t;throw Error("The input selector at index "+o+" for '"+n+"' is missing from the object passed to resolveSelectors()")})};for(var o in e)n(o);if(!r)throw Error("You must pass at least one real selector. If they're all string references there's no");for(var a,c=function(){var r=!1;for(var n in e){var o=e[n];t(n)||(r=!0,o.deps.every(t)&&(e[n]=o(e,o.deps)))}return r};c();)if(a||(a=Date.now()),Date.now()-a>500)throw Error("Could not resolve selector dependencies.");return e},W=!1;try{W=!!window.localStorage.debug}catch(G){}var V,$=W||!1,X="undefined"!=typeof window,Q=X||"undefined"!=typeof self,z=function(e){setTimeout(e,0)},K=Q&&self.requestAnimationFrame?self.requestAnimationFrame:z,Y=Q&&self.requestIdleCallback?self.requestIdleCallback:z,J=function(){var e=!1;try{var t=Object.defineProperty({},"passive",{get:function(){e=!0}});window.addEventListener("test",t,t),window.removeEventListener("test",t,t)}catch(t){e=!1}return e},Z=J(),ee=function(e,t){return e.substr(0,t.length)===t},te=function(e){var t={};for(var r in e)Object.assign(t,e[r]);return t},re=function(e){var t=[];for(var r in e)t.push.apply(t,e[r]);return t},ne=function(e,t,r){void 0===r&&(r={passive:!1}),Q&&(r.passive?Z?self.addEventListener(e,t,{passive:!0}):self.addEventListener(e,ae(t,200),!1):self.addEventListener(e,t))},oe=function(e){var t="s"===e[0]?6:5;return e[t].toLowerCase()+e.slice(t+1)},ae=function(e,t){var r,n=function(){var n=this,o=arguments;clearTimeout(r),r=setTimeout(function(){e.apply(n,o)},t)};return n.cancel=function(){clearTimeout(r)},n},ce=function(){history.replaceState({height:document.body.offsetHeight,width:document.body.offsetWidth,y:document.body.scrollTop,x:document.body.scrollLeft},"")},ie=function(){var e=history.state;e&&(document.body.setAttribute("style","height: "+e.height+"px; width: "+e.width+"px;"),window.scrollTo(e.x,e.y),Y(function(){return document.body.removeAttribute("style")}))},ue=function(){X&&(history.scrollRestoration&&(history.scrollRestoration="manual"),ne("popstate",ie),ne("scroll",ae(ce,300),{passive:!0}),ie())},se=function(e){var t=e.name;if(!t)throw TypeError('bundles must have a "name" property');var r={name:t,reducer:e.reducer||e.getReducer&&e.getReducer()||null,init:e.init||null,extraArgCreators:e.getExtraArgs||null,middlewareCreators:e.getMiddleware,actionCreators:null,selectors:null,reactorNames:null,rawBundle:e};return Object.keys(e).forEach(function(t){if(ee(t,"do"))(r.actionCreators||(r.actionCreators={}))[t]=e[t];else{var n=ee(t,"select"),o=ee(t,"react");(n||o)&&((r.selectors||(r.selectors={}))[t]=e[t],o&&(r.reactorNames||(r.reactorNames=[])).push(t))}}),r},le=function(e){var t={bundleNames:[],reducers:{},selectors:{},actionCreators:{},rawBundles:[],processedBundles:[],initMethods:[],middlewareCreators:[],extraArgCreators:[],reactorNames:[]};return e.map(se).forEach(function(e){var r;t.bundleNames.push(e.name),Object.assign(t.selectors,e.selectors),Object.assign(t.actionCreators,e.actionCreators),e.reducer&&Object.assign(t.reducers,((V={})[e.name]=e.reducer,V)),e.init&&t.initMethods.push(e.init),e.middlewareCreators&&t.middlewareCreators.push(e.middlewareCreators),e.extraArgCreators&&t.extraArgCreators.push(e.extraArgCreators),e.reactorNames&&(r=t.reactorNames).push.apply(r,e.reactorNames),t.processedBundles.push(e),t.rawBundles.push(e.rawBundle)}),t},fe=function(e,t){e.meta||(e.meta={chunks:[],unboundSelectors:{},unboundActionCreators:{},reactorNames:[]});var r=e.meta;r.chunks.push(t);var n=Object.assign(r.unboundSelectors,t.selectors);M(n),r.unboundSelectors=n,function(e,t){var r=function(r){var n=t[r];e[r]||(e[r]=function(){return n(e.getState())})};for(var n in t)r(n)}(e,n),r.reactorNames=r.reactorNames.concat(t.reactorNames),Object.assign(r.unboundActionCreators,t.actionCreators),Object.assign(e,P(t.actionCreators,e.dispatch)),t.initMethods.forEach(function(t){return t(e)})},de=function(e){return function(t,r){return"BATCH_ACTIONS"===r.type?r.actions.reduce(e,t):e(t,r)}},pe=function(){for(var e=[],t=arguments.length;t--;)e[t]=arguments[t];var r=le(e);return function(e){var t,n=j(de(N(r.reducers)),e,function(){for(var e=[],t=arguments.length;t--;)e[t]=arguments[t];return function(t){return function(r,n,o){var a,c,i=t(r,n,o);return c=e.map(function(e){return e(i)}),a=U.apply(void 0,c)(i.dispatch),Object.assign(i,{dispatch:a})}}}.apply(void 0,[function(e){return function(t){return function(r){var n=r.actionCreator,o=r.args;if(n){var a=e.meta.unboundActionCreators[n];if(!a)throw Error("NoSuchActionCreator: "+n);return t(o?a.apply(void 0,o):a())}return t(r)}}},(t=r.extraArgCreators,function(e){var r=t.reduce(function(t,r){return Object.assign(t,r(e))},{});return function(t){return function(n){return"function"==typeof n?n(Object.assign({},{getState:e.getState,dispatch:e.dispatch,store:e},r)):t(n)}}})].concat(r.middlewareCreators.map(function(e){return e(r)}))));return n.select=function(e){return e.reduce(function(e,t){if(!n[t])throw Error("SelectorNotFound "+t);return e[oe(t)]=n[t](),e},{})},n.selectAll=function(){return n.select(Object.keys(n.meta.unboundSelectors))},n.action=function(e,t){return n[e].apply(n,t)},function(e){e.subscriptions={watchedValues:{}};var t=e.subscriptions.set=new Set,r=e.subscriptions.watchedSelectors={},n=function(e){r[e]=(r[e]||0)+1},o=function(e){var t=r[e]-1;0===t?delete r[e]:r[e]=t};e.subscribe(function(){var n=r.all?e.selectAll():e.select(Object.keys(r)),o=e.subscriptions.watchedValues,a={};for(var c in n){var i=n[c];i!==o[c]&&(a[c]=i)}e.subscriptions.watchedValues=n,t.forEach(function(e){var t={},r=!1;"all"===e.names?(Object.assign(t,a),r=!!Object.keys(t).length):e.names.forEach(function(e){a.hasOwnProperty(e)&&(t[e]=a[e],r=!0)}),r&&e.fn(t)})}),e.subscribeToAllChanges=function(t){return e.subscribeToSelectors("all",t)},e.subscribeToSelectors=function(r,a){var c="all"===r,i={fn:a,names:c?"all":r.map(oe)};return t.add(i),c?n("all"):r.forEach(n),Object.assign(e.subscriptions.watchedValues,c?e.selectAll():e.select(r)),function(){t.delete(i),c?o("all"):r.forEach(o)}}}(n),fe(n,r),n.integrateBundles=function(){for(var e=[],t=arguments.length;t--;)e[t]=arguments[t];fe(n,le(e));var r=n.meta.chunks.reduce(function(e,t){return Object.assign(e,t.reducers)},{});n.replaceReducer(de(N(r)))},n}},he=/\((.*?)\)/g,ve=/(\(\?)?:\w+/g,ye=/[\-{}\[\]+?.,\\\^$|#\s]/g,ge=/\*/g,me=function(e,t){var r=Object.keys(e);for(var n in e)e[n]={value:e[n]};return function(n){var o,a;return r.some(function(t){var r,c,i;(a=e[t]).regExp||(i=[],c=(c=t).replace(ye,"\\$&").replace(he,"(?:$1)?").replace(ve,function(e,t){return i.push(e.slice(1)),t?e:"([^/?]+)"}).replace(ge,function(e,t){return i.push("path"),"([^?]*?)"}),r={regExp:new RegExp("^"+c+"(?:\\?([\\s\\S]*))?$"),namedParams:i},a.regExp=r.regExp,a.namedParams=r.namedParams,a.pattern=t);var u=a.regExp.exec(n);if(u)return u=u.slice(1,-1),o=u.reduce(function(e,t,r){return t&&(e[a.namedParams[r]]=t),e},{}),!0})?{page:a.value,params:o,url:n,pattern:a.pattern}:t?{page:t,url:n,params:null}:null}},be={name:null,getPromise:null,actionBaseType:null,staleAfter:9e5,retryAfter:6e4,expireAfter:1/0,checkIfOnline:!0,persist:!0};function Ee(e){var t=Object.assign({},be,e),r=t.name,n=t.staleAfter,o=t.retryAfter,a=t.actionBaseType,c=t.checkIfOnline,i=t.expireAfter,u=r.charAt(0).toUpperCase()+r.slice(1),s=a||r.toUpperCase(),l=function(e){return e[r]},f=function(e){return e[r].data},d=function(e){return e[r].lastSuccess},p=q(l,function(e){return e.errorTimes.slice(-1)[0]||null}),h=q(l,d,"selectAppTime",function(e,t,r){return!!e.isOutdated||!!t&&r-t>n}),v=q(p,"selectAppTime",function(e,t){return!!e&&t-e<o}),y=q(l,function(e){return e.isLoading}),g=q(l,function(e){return e.failedPermanently}),m=q(y,g,v,f,h,"selectIsOnline",function(e,t,r,n,o,a){return!(c&&!a||e||t||r)&&(!n||o)}),b={STARTED:s+"_FETCH_STARTED",FINISHED:s+"_FETCH_FINISHED",FAILED:s+"_FETCH_FAILED",CLEARED:s+"_CLEARED",OUTDATED:s+"_OUTDATED",EXPIRED:s+"_EXPIRED"},E=function(){return{type:b.EXPIRED}},w={data:null,errorTimes:[],errorType:null,lastSuccess:null,isOutdated:!1,isLoading:!1,isExpired:!1,failedPermanently:!1},A={name:r,reducer:function(e,t){void 0===e&&(e=w);var r,n=t.type,o=t.payload,a=t.error,c=t.merge;if(n===b.STARTED)return Object.assign({},e,{isLoading:!0});if(n===b.FINISHED)return r=c?Object.assign({},e.data,o):o,Object.assign({},e,{isLoading:!1,data:r,lastSuccess:Date.now(),errorTimes:[],errorType:null,failedPermanently:!1,isOutdated:!1,isExpired:!1});if(n===b.FAILED){var i=a&&a.message||a;return Object.assign({},e,{isLoading:!1,errorTimes:e.errorTimes.concat([Date.now()]),errorType:i,failedPermanently:!(!a||!a.permanent)})}return n===b.CLEARED?w:n===b.EXPIRED?Object.assign({},w,{isExpired:!0,errorTimes:e.errorTimes,errorType:e.errorType}):n===b.OUTDATED?Object.assign({},e,{isOutdated:!0}):e}};return A["select"+u+"Raw"]=l,A["select"+u]=f,A["select"+u+"IsStale"]=h,A["select"+u+"IsExpired"]=function(e){return e[r].isExpired},A["select"+u+"LastError"]=p,A["select"+u+"IsWaitingToRetry"]=v,A["select"+u+"IsLoading"]=y,A["select"+u+"FailedPermanently"]=g,A["select"+u+"ShouldUpdate"]=m,A["doFetch"+u]=function(){return function(e){var r=e.dispatch;return r({type:b.STARTED}),t.getPromise(e).then(function(e){r(function(e){return{type:b.FINISHED,payload:e}}(e))},function(e){r(function(e){return{type:b.FAILED,error:e}}(e))})}},A["doMark"+u+"AsOutdated"]=function(){return{type:b.OUTDATED}},A["doClear"+u]=function(){return{type:b.CLEARED}},A["doExpire"+u]=E,t.persist&&(A.persistActions=[b.FINISHED,b.EXPIRED,b.OUTDATED,b.CLEARED]),1/0!==i&&(A["reactExpire"+u]=q(d,"selectAppTime",function(e,t){return!!e&&(t-e>i?E():void 0)})),A}var we=!("undefined"==typeof window&&"undefined"==typeof self),Ae="undefined"==typeof requestIdleCallback?function(e){return setTimeout(e,0)}:requestIdleCallback,xe=function(e,t){void 0===t&&(t=!1);var r=new Error(e);return t&&(r.permanent=!0),r},Te=["An unknown geolocation error occured","Geolocation permission denied","Geolocation unavailable","Geolocation request timed out"],Oe={timeout:6e4,enableHighAccuracy:!1,persist:!0,staleAge:9e5,retryAfter:6e4},Se={idleTimeout:3e4,idleAction:"APP_IDLE",doneCallback:null,stopWhenTabInactive:!0},Ie={timeout:500},Re=function(e,t,r){return ae(function(){e?K(function(){return Y(r,Ie)}):Y(r,Ie)},t)};function je(e){return{name:"reactors",init:function(t){var r,n=Object.assign({},Se,e),o=n.idleAction,a=n.idleTimeout;a&&(r=Re(n.stopWhenTabInactive,a,function(){return t.dispatch({type:o})}));var c=function(){t.nextReaction||(t.meta.reactorNames.some(function(e){var r=t[e]();return r&&(t.activeReactor=e,t.nextReaction=r),r}),t.nextReaction&&Y(function(){var e=t.nextReaction;t.activeReactor=null,t.nextReaction=null,t.dispatch(e)},Ie)),r&&(r(),Q||t.nextReaction||t.selectAsyncActive&&t.selectAsyncActive()||(r&&r.cancel(),n.doneCallback&&n.doneCallback()))};t.subscribe(c),c()}}}var Ce=Object.prototype.hasOwnProperty,De={stringify:function(e,t){t=t||"";var r=[];for(var n in"string"!=typeof t&&(t="?"),e)Ce.call(e,n)&&r.push(encodeURIComponent(n)+"="+encodeURIComponent(e[n]));return r.length?t+r.join("&"):""},parse:function(e){for(var t,r=/([^=?&]+)=?([^&]*)/g,n={};t=r.exec(e);n[decodeURIComponent(t[1])]=decodeURIComponent(t[2]));return n}},Ne=function(e){return"[object String]"===Object.prototype.toString.call(e)},Le=function(e){return void 0!==e},Pe=function(e){return Ne(e)?e:De.stringify(e)},Ue=/^[0-9.]+$/,Be=function(e,t){if(Ue.test(e))return[];var r=e.split(".");return t?r.slice(-2).join("."):e.split(".").slice(0,-2)},Fe=function(e,t){return t.charAt(0)===e?t.slice(1):t},_e=function(e,t){return t===e||""===t?"":t.charAt(0)!==e?e+t:t},ke=X?window.location:{},He={name:"url",inert:!X,actionType:"URL_UPDATED",handleScrollRestoration:!0},Ge=function(e){var t={};for(var r in e){var n=e[r];Ne(n)&&(t[r]=n)}return t};function qe(e){var t=Object.assign({},He,e),r=t.actionType,n=function(e){return e[t.name]},o=q(n,function(e){return Ge(new URL(e.url))}),a=q(o,function(e){return De.parse(e.search)}),c=q(a,function(e){return De.stringify(e)}),i=q(o,function(e){return e.pathname}),u=q(o,function(e){return Fe("#",e.hash)}),s=q(u,function(e){return De.parse(e)}),l=q(o,function(e){return e.hostname}),f=q(l,function(e){return Be(e)}),d=function(e,t){return void 0===t&&(t={replace:!1}),function(o){var a=o.dispatch,c=o.getState,i=e;if("string"==typeof e){var u=new URL("/"===e.charAt(0)?"http://example.com"+e:e);i={pathname:u.pathname,query:u.search||"",hash:u.hash||""}}var s=new URL(n(c()).url);Le(i.pathname)&&(s.pathname=i.pathname),Le(i.hash)&&(s.hash=Pe(i.hash)),Le(i.query)&&(s.search=Pe(i.query)),a({type:r,payload:{url:s.href,replace:t.replace}})}};return{name:t.name,init:function(e){if(!t.inert){t.handleScrollRestoration&&ue(),window.addEventListener("popstate",function(){e.doUpdateUrl({pathname:ke.pathname,hash:ke.hash,query:ke.search})});var r=e.selectUrlRaw();e.subscribe(function(){var n=e.selectUrlRaw();if(r!==n&&n.url!==ke.href)try{window.history[n.replace?"replaceState":"pushState"]({},null,n.url),t.handleScrollRestoration&&ce(),document.body.scrollTop=0,document.body.scrollLeft=0}catch(e){console.error(e)}r=n})}},getReducer:function(){var e={url:!t.inert&&X?ke.href:"/",replace:!1};return function(t,n){void 0===t&&(t=e);var o=n.type,a=n.payload;return"@@redux/INIT"===o&&"string"==typeof t?{url:t,replace:!1}:o===r?Object.assign({url:a.url||a,replace:!!a.replace}):t}},doUpdateUrl:d,doReplaceUrl:function(e){return d(e,{replace:!0})},doUpdateQuery:function(e,t){return void 0===t&&(t={replace:!0}),d({query:Pe(e)},t)},doUpdateHash:function(e,t){return void 0===t&&(t={replace:!1}),d({hash:_e("#",Pe(e))},t)},selectUrlRaw:n,selectUrlObject:o,selectQueryObject:a,selectQueryString:c,selectPathname:i,selectHash:u,selectHashObject:s,selectHostname:l,selectSubdomains:f}}function Me(e){return function(t){return function(r){var n=e.getState().debug;n&&(console.group(r.type),console.info("action:",r));var o=t(r);return n&&(console.debug("state:",e.getState()),self.logSelectors&&self.logSelectors(),self.logNextReaction&&self.logNextReaction(),console.groupEnd(r.type)),o}}}var We={name:"debug",reducer:function(e,t){void 0===e&&(e=$);var r=t.type;return"DEBUG_ENABLED"===r||"DEBUG_DISABLED"!==r&&e},doEnableDebug:function(){return{type:"DEBUG_ENABLED"}},doDisableDebug:function(){return{type:"DEBUG_DISABLED"}},selectIsDebug:function(e){return e.debug},getMiddleware:function(){return Me},init:function(e){if(e.selectIsDebug()){var t=e.meta.chunks[0].bundleNames;self.store=e;var r=[];for(var n in e)0===n.indexOf("do")&&r.push(n);r.sort(),e.logSelectors=self.logSelectors=function(){e.selectAll&&console.log("%cselectors:","color: #4CAF50;",e.selectAll())},e.logBundles=self.logBundles=function(){console.log("%cinstalled bundles:\n  %c%s","color: #1676D2;","color: black;",t.join("\n  "))},e.logActionCreators=self.logActionCreators=function(){console.groupCollapsed("%caction creators","color: #F57C00;"),r.forEach(function(e){return console.log(e)}),console.groupEnd()},e.logReactors=self.logReactors=function(){console.groupCollapsed("%creactors","color: #F57C00;"),e.meta.reactorNames.forEach(function(e){return console.log(e)}),console.groupEnd()},e.logNextReaction=self.logNextReaction=function(){var t=e.nextReaction;t&&console.log("%cnext reaction:\n  %c"+e.activeReactor,"color: #F57C00;","color: black;",t)},console.groupCollapsed("%credux bundler","color: #1676D2;"),e.logBundles(),e.logSelectors(),e.logReactors(),console.groupEnd(),e.isReacting&&console.log("%cqueuing reaction:","color: #F57C00;")}}},Ve={name:"online",selectIsOnline:function(e){return e.online},reducer:function(e,t){void 0===e&&(e=!0);var r=t.type;return"OFFLINE"!==r&&("ONLINE"===r||e)},init:function(e){ne("online",function(){return e.dispatch({type:"ONLINE"})}),ne("offline",function(){return e.dispatch({type:"OFFLINE"})})}},$e=t,Xe=o,Qe=function(e){return{name:"localCache",getMiddleware:function(t){var r,n,o,a,c={};return t.rawBundles.forEach(function(e){e.persistActions&&e.persistActions.forEach(function(t){c[t]||(c[t]=[]),c[t].push(e.name)})}),n=(r={actionMap:c,cacheFn:e}).cacheFn,o=r.actionMap,a=r.logger,function(e){var t=e.getState;return function(e){return function(r){var c=o[r.type],i=e(r),u=t();return we&&c&&Ae(function(){Promise.all(c.map(function(e){return n(e,u[e])})).then(function(){a&&a("cached "+c.join(", ")+" due to "+r.type)})},{timeout:500}),i}}}}}},ze=function(e){return{name:"routes",selectRouteInfo:q("selectPathname",me(e)),selectRouteParams:q("selectRouteInfo",function(e){return e.params}),selectRoute:q("selectRouteInfo",function(e){return e.page})}},Ke=Ee,Ye=je,Je=Re,Ze=Ve,et=qe,tt=We,rt=pe,nt=function(e){var t=Object.assign({},Oe,e);return Ee({name:"geolocation",actionBaseType:"GEOLOCATION_REQUEST",getPromise:function(){return new Promise(function(e,r){Q&&navigator.geolocation||r(xe("Geolocation not supported",!0)),navigator.geolocation.getCurrentPosition(function(t){var r={},n=t.coords;for(var o in n)r[o]=n[o];r.timestamp=t.timestamp,e(r)},function(e){var t=e.code;r(xe(Te[t],1===t))},{timeout:t.timeout,enableHighAccuracy:t.enableHighAccuracy})})},persist:t.persist,staleAge:t.staleAge,retryAfter:t.retryAfter})},ot=function(){for(var e=[],r=arguments.length;r--;)e[r]=arguments[r];e||(e=[]);var n=[t,o,Ve,qe(),je(),We].concat(e);return pe.apply(void 0,n)};exports.appTimeBundle=$e,exports.asyncCountBundle=Xe,exports.createCacheBundle=Qe,exports.createRouteBundle=ze,exports.createAsyncResourceBundle=Ke,exports.createReactorBundle=Ye,exports.getIdleDispatcher=Je,exports.onlineBundle=Ze,exports.createUrlBundle=et,exports.debugBundle=tt,exports.composeBundlesRaw=rt,exports.createGeolocationBundle=nt,exports.composeBundles=ot,exports.createSelector=q,exports.resolveSelectors=M,exports.HAS_DEBUG_FLAG=$,exports.HAS_WINDOW=X,exports.IS_BROWSER=Q,exports.raf=K,exports.ric=Y,exports.isPassiveSupported=J,exports.PASSIVE_EVENTS_SUPPORTED=Z,exports.startsWith=ee,exports.flattenExtractedToObject=te,exports.flattenExtractedToArray=re,exports.addGlobalListener=ne,exports.selectorNameToValueName=oe,exports.debounce=ae,exports.saveScrollPosition=ce,exports.restoreScrollPosition=ie,exports.initScrollPosition=ue,exports.createStore=j,exports.combineReducers=N,exports.bindActionCreators=P,exports.applyMiddleware=F,exports.compose=U;
},{}],13:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0});var e=require("redux-bundler");exports.default={name:"sorghumbase",getReducer:function(){var e={data:null,loading:!1};return function(){var a=arguments.length>0&&void 0!==arguments[0]?arguments[0]:e,r=arguments[1],t=r.type,n=r.payload;return"SEARCH_START"===t?Object.assign({},a,{loading:!0}):"SEARCH_SUCCESS"===t?Object.assign({},a,{loading:!1,data:n}):a}},doSearchSorghumbase:function(e,a){return function(r){var t=r.dispatch,n=r.sbSearch;t({type:"SEARCH_START"}),n(e,a).then(function(e){t({type:"SEARCH_SUCCESS",payload:e})})}},selectSearchData:function(e){return e.sorghumbase},reactShouldSearch:(0,e.createSelector)("selectSearchData",function(e){return!e.loading&&!e.data&&{actionCreator:"doSearchSorghumbase",args:[e.category,e.query]}})};
},{"redux-bundler":17}],14:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0}),exports.default={name:"extra-args",getExtraArgs:function(e){return{sbSearch:function(e,t){return fetch("/search_api/"+e+"?q="+t).then(function(e){return e.json()}).catch(function(e){throw e})}}}};
},{}],7:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0});var e=require("redux-bundler"),r=require("./sorghumbase"),u=d(r),t=require("./extra-args"),s=d(t);function d(e){return e&&e.__esModule?e:{default:e}}exports.default=(0,e.composeBundles)(u.default,s.default);
},{"redux-bundler":17,"./sorghumbase":13,"./extra-args":14}],11:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0}),exports.connect=exports.Provider=void 0;var t=require("preact"),e=function(){};e.prototype.getChildContext=function(){return{store:this.props.store}},e.prototype.render=function(t){return t.children[0]};var r=function(){for(var e=[],r=arguments.length;r--;)e[r]=arguments[r];var o=e.slice(-1)[0],n=[],s=[];return(e.length>1?e.slice(0,-1):[]).forEach(function(t){if("select"!==t.slice(0,6)){if("do"!==t.slice(0,2))throw Error("CanNotConnect "+t);n.push(t)}else s.push(t)}),function(e){function r(t,r){var o=this;e.call(this,t,r);var i=r.store;this.state=i.select(s),this.unsubscribe=i.subscribeToSelectors(s,this.setState.bind(this)),this.actionCreators={},n.forEach(function(t){o.actionCreators[t]=function(){for(var e=[],r=arguments.length;r--;)e[r]=arguments[r];return i[t].apply(i,e)}})}return e&&(r.__proto__=e),r.prototype=Object.create(e&&e.prototype),r.prototype.constructor=r,r.prototype.componentWillUnmount=function(){this.unsubscribe()},r.prototype.render=function(e,r){return(0,t.h)(o,Object.assign({},e,r,this.actionCreators))},r}(t.Component)};exports.Provider=e,exports.connect=r;
},{"preact":5}],9:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0});var e=require("redux-bundler-preact"),r=require("preact"),t=function(e){var t=e.searchData;return(0,r.h)("div",null,!t&&(0,r.h)("p",null,"No data yet"),t&&t.loading&&(0,r.h)("p",null,"Loading"),t&&t.data&&(0,r.h)("code",null,JSON.stringify(t,null,"  ")))};exports.default=(0,e.connect)("selectSearchData",t);
},{"redux-bundler-preact":11,"preact":5}],3:[function(require,module,exports) {
"use strict";Object.defineProperty(exports,"__esModule",{value:!0});var e=require("preact"),r=require("redux-bundler-preact"),u=require("./results"),t=l(u);function l(e){return e&&e.__esModule?e:{default:e}}exports.default=function(u){return(0,e.h)(r.Provider,{store:u},(0,e.h)(t.default,null))};
},{"preact":5,"redux-bundler-preact":11,"./results":9}],1:[function(require,module,exports) {
"use strict";var e=require("preact"),r=require("./bundles"),u=a(r),t=require("./components/root"),o=a(t);function a(e){return e&&e.__esModule?e:{default:e}}window.searchCategory=function(r,t,a){var n={sorghumbase:{category:r,query:t}};(0,e.render)((0,o.default)((0,u.default)(n)),a)};
},{"preact":5,"./bundles":7,"./components/root":3}]},{},[1], null)
//# sourceMappingURL=./search.map