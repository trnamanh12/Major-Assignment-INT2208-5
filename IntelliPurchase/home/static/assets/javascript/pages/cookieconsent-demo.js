"use strict";function _classCallCheck(e,n){if(!(e instanceof n))throw new TypeError("Cannot call a class as a function")}function _defineProperties(e,n){for(var o=0;o<n.length;o++){var t=n[o];t.enumerable=t.enumerable||!1,t.configurable=!0,"value"in t&&(t.writable=!0),Object.defineProperty(e,t.key,t)}}function _createClass(e,n,o){return n&&_defineProperties(e.prototype,n),o&&_defineProperties(e,o),e}var CookieconsentDemo=function(){function e(){_classCallCheck(this,e),this.init()}return _createClass(e,[{key:"init",value:function(){this.handleCookie()}},{key:"handleCookie",value:function(){window.cookieconsent.initialise({container:document.querySelector("#cookieDemo"),palette:{popup:{background:"#131D28"},button:{background:"#F7C46C"}},revokable:!1,onStatusChange:function(){console.log(this.hasConsented()?"enable cookies":"disable cookies")},law:{regionalLaw:!1},location:!1,content:{message:"Trang web này sử dụng cookie để đảm bảo bạn có được trải nghiệm tốt nhất trên trang web của chúng tôi.",dismiss:"Đã hiểu, Đóng"}})}}]),e}();$(document).on("theme:init",function(){new CookieconsentDemo});