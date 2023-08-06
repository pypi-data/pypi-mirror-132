/*! For license information please see de84290e.js.LICENSE.txt */
"use strict";(self.webpackChunkhome_assistant_frontend=self.webpackChunkhome_assistant_frontend||[]).push([[43376],{35854:(e,t,r)=>{r.d(t,{G:()=>n,R:()=>a});r(65233);var i=r(21006),o=r(98235);const n={properties:{checked:{type:Boolean,value:!1,reflectToAttribute:!0,notify:!0,observer:"_checkedChanged"},toggles:{type:Boolean,value:!0,reflectToAttribute:!0},value:{type:String,value:"on",observer:"_valueChanged"}},observers:["_requiredChanged(required)"],created:function(){this._hasIronCheckedElementBehavior=!0},_getValidity:function(e){return this.disabled||!this.required||this.checked},_requiredChanged:function(){this.required?this.setAttribute("aria-required","true"):this.removeAttribute("aria-required")},_checkedChanged:function(){this.active=this.checked,this.fire("iron-change")},_valueChanged:function(){void 0!==this.value&&null!==this.value||(this.value="on")}},a=[i.V,o.x,n]},62132:(e,t,r)=>{r.d(t,{K:()=>s});r(65233);var i=r(35854),o=r(49075),n=r(84938);const a={_checkedChanged:function(){i.G._checkedChanged.call(this),this.hasRipple()&&(this.checked?this._ripple.setAttribute("checked",""):this._ripple.removeAttribute("checked"))},_buttonStateChanged:function(){n.o._buttonStateChanged.call(this),this.disabled||this.isAttached&&(this.checked=this.active)}},s=[o.B,i.R,a]},32296:(e,t,r)=>{r(65233);var i=r(62132),o=r(49075),n=r(9672),a=r(50856),s=r(87529);const c=a.d`<style>
  :host {
    display: inline-block;
    white-space: nowrap;
    cursor: pointer;
    --calculated-paper-checkbox-size: var(--paper-checkbox-size, 18px);
    /* -1px is a sentinel for the default and is replaced in \`attached\`. */
    --calculated-paper-checkbox-ink-size: var(--paper-checkbox-ink-size, -1px);
    @apply --paper-font-common-base;
    line-height: 0;
    -webkit-tap-highlight-color: transparent;
  }

  :host([hidden]) {
    display: none !important;
  }

  :host(:focus) {
    outline: none;
  }

  .hidden {
    display: none;
  }

  #checkboxContainer {
    display: inline-block;
    position: relative;
    width: var(--calculated-paper-checkbox-size);
    height: var(--calculated-paper-checkbox-size);
    min-width: var(--calculated-paper-checkbox-size);
    margin: var(--paper-checkbox-margin, initial);
    vertical-align: var(--paper-checkbox-vertical-align, middle);
    background-color: var(--paper-checkbox-unchecked-background-color, transparent);
  }

  #ink {
    position: absolute;

    /* Center the ripple in the checkbox by negative offsetting it by
     * (inkWidth - rippleWidth) / 2 */
    top: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    left: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    width: var(--calculated-paper-checkbox-ink-size);
    height: var(--calculated-paper-checkbox-ink-size);
    color: var(--paper-checkbox-unchecked-ink-color, var(--primary-text-color));
    opacity: 0.6;
    pointer-events: none;
  }

  #ink:dir(rtl) {
    right: calc(0px - (var(--calculated-paper-checkbox-ink-size) - var(--calculated-paper-checkbox-size)) / 2);
    left: auto;
  }

  #ink[checked] {
    color: var(--paper-checkbox-checked-ink-color, var(--primary-color));
  }

  #checkbox {
    position: relative;
    box-sizing: border-box;
    height: 100%;
    border: solid 2px;
    border-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
    border-radius: 2px;
    pointer-events: none;
    -webkit-transition: background-color 140ms, border-color 140ms;
    transition: background-color 140ms, border-color 140ms;

    -webkit-transition-duration: var(--paper-checkbox-animation-duration, 140ms);
    transition-duration: var(--paper-checkbox-animation-duration, 140ms);
  }

  /* checkbox checked animations */
  #checkbox.checked #checkmark {
    -webkit-animation: checkmark-expand 140ms ease-out forwards;
    animation: checkmark-expand 140ms ease-out forwards;

    -webkit-animation-duration: var(--paper-checkbox-animation-duration, 140ms);
    animation-duration: var(--paper-checkbox-animation-duration, 140ms);
  }

  @-webkit-keyframes checkmark-expand {
    0% {
      -webkit-transform: scale(0, 0) rotate(45deg);
    }
    100% {
      -webkit-transform: scale(1, 1) rotate(45deg);
    }
  }

  @keyframes checkmark-expand {
    0% {
      transform: scale(0, 0) rotate(45deg);
    }
    100% {
      transform: scale(1, 1) rotate(45deg);
    }
  }

  #checkbox.checked {
    background-color: var(--paper-checkbox-checked-color, var(--primary-color));
    border-color: var(--paper-checkbox-checked-color, var(--primary-color));
  }

  #checkmark {
    position: absolute;
    width: 36%;
    height: 70%;
    border-style: solid;
    border-top: none;
    border-left: none;
    border-right-width: calc(2/15 * var(--calculated-paper-checkbox-size));
    border-bottom-width: calc(2/15 * var(--calculated-paper-checkbox-size));
    border-color: var(--paper-checkbox-checkmark-color, white);
    -webkit-transform-origin: 97% 86%;
    transform-origin: 97% 86%;
    box-sizing: content-box; /* protect against page-level box-sizing */
  }

  #checkmark:dir(rtl) {
    -webkit-transform-origin: 50% 14%;
    transform-origin: 50% 14%;
  }

  /* label */
  #checkboxLabel {
    position: relative;
    display: inline-block;
    vertical-align: middle;
    padding-left: var(--paper-checkbox-label-spacing, 8px);
    white-space: normal;
    line-height: normal;
    color: var(--paper-checkbox-label-color, var(--primary-text-color));
    @apply --paper-checkbox-label;
  }

  :host([checked]) #checkboxLabel {
    color: var(--paper-checkbox-label-checked-color, var(--paper-checkbox-label-color, var(--primary-text-color)));
    @apply --paper-checkbox-label-checked;
  }

  #checkboxLabel:dir(rtl) {
    padding-right: var(--paper-checkbox-label-spacing, 8px);
    padding-left: 0;
  }

  #checkboxLabel[hidden] {
    display: none;
  }

  /* disabled state */

  :host([disabled]) #checkbox {
    opacity: 0.5;
    border-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
  }

  :host([disabled][checked]) #checkbox {
    background-color: var(--paper-checkbox-unchecked-color, var(--primary-text-color));
    opacity: 0.5;
  }

  :host([disabled]) #checkboxLabel  {
    opacity: 0.65;
  }

  /* invalid state */
  #checkbox.invalid:not(.checked) {
    border-color: var(--paper-checkbox-error-color, var(--error-color));
  }
</style>

<div id="checkboxContainer">
  <div id="checkbox" class$="[[_computeCheckboxClass(checked, invalid)]]">
    <div id="checkmark" class$="[[_computeCheckmarkClass(checked)]]"></div>
  </div>
</div>

<div id="checkboxLabel"><slot></slot></div>`;c.setAttribute("strip-whitespace",""),(0,n.k)({_template:c,is:"paper-checkbox",behaviors:[i.K],hostAttributes:{role:"checkbox","aria-checked":!1,tabindex:0},properties:{ariaActiveAttribute:{type:String,value:"aria-checked"}},attached:function(){(0,s.T8)(this,(function(){if("-1px"===this.getComputedStyleValue("--calculated-paper-checkbox-ink-size").trim()){var e=this.getComputedStyleValue("--calculated-paper-checkbox-size").trim(),t="px",r=e.match(/[A-Za-z]+$/);null!==r&&(t=r[0]);var i=parseFloat(e),o=8/3*i;"px"===t&&(o=Math.floor(o))%2!=i%2&&o++,this.updateStyles({"--paper-checkbox-ink-size":o+t})}}))},_computeCheckboxClass:function(e,t){var r="";return e&&(r+="checked "),t&&(r+="invalid"),r},_computeCheckmarkClass:function(e){return e?"":"hidden"},_createRipple:function(){return this._rippleContainer=this.$.checkboxContainer,o.S._createRipple.call(this)}})},73826:(e,t,r)=>{r.d(t,{f:()=>m});var i=r(5701);function o(e,t,r,i){var o=n();if(i)for(var d=0;d<i.length;d++)o=i[d](o);var h=t((function(e){o.initializeInstanceElements(e,p.elements)}),r),p=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(l(n.descriptor)||l(o.descriptor)){if(c(n)||c(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(c(n)){if(c(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}s(n,o)}else t.push(n)}return t}(h.d.map(a)),e);return o.initializeClassElements(h.F,p.elements),o.runClassFinishers(h.F,p.finishers)}function n(){n=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!c(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,o[n])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return p(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?p(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=h(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:d(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=d(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function a(e){var t,r=h(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function s(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function c(e){return e.decorators&&e.decorators.length}function l(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function d(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function h(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function p(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function u(e,t,r){return u="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=f(e)););return e}(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(r):o.value}},u(e,t,r||e)}function f(e){return f=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},f(e)}const m=e=>o(null,(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,i.C)({attribute:!1})],key:"hass",value:void 0},{kind:"field",key:"__unsubs",value:void 0},{kind:"method",key:"connectedCallback",value:function(){u(f(r.prototype),"connectedCallback",this).call(this),this.__checkSubscribed()}},{kind:"method",key:"disconnectedCallback",value:function(){if(u(f(r.prototype),"disconnectedCallback",this).call(this),this.__unsubs){for(;this.__unsubs.length;){const e=this.__unsubs.pop();e instanceof Promise?e.then((e=>e())):e()}this.__unsubs=void 0}}},{kind:"method",key:"updated",value:function(e){u(f(r.prototype),"updated",this).call(this,e),e.has("hass")&&this.__checkSubscribed()}},{kind:"method",key:"hassSubscribe",value:function(){return[]}},{kind:"method",key:"__checkSubscribed",value:function(){void 0===this.__unsubs&&this.isConnected&&void 0!==this.hass&&(this.__unsubs=this.hassSubscribe())}}]}}),e)},43376:(e,t,r)=>{r.r(t);r(32296);var i=r(7599),o=r(26767),n=r(5701),a=r(17717),s=r(67352),c=r(228),l=r(1460),d=r(86230),h=r(62877);r(22098),r(55905);const p=(e,t,r)=>e.callWS({type:"shopping_list/items/update",item_id:t,...r});var u=r(73826);function f(){f=function(){return e};var e={elementsDefinitionOrder:[["method"],["field"]],initializeInstanceElements:function(e,t){["method","field"].forEach((function(r){t.forEach((function(t){t.kind===r&&"own"===t.placement&&this.defineClassElement(e,t)}),this)}),this)},initializeClassElements:function(e,t){var r=e.prototype;["method","field"].forEach((function(i){t.forEach((function(t){var o=t.placement;if(t.kind===i&&("static"===o||"prototype"===o)){var n="static"===o?e:r;this.defineClassElement(n,t)}}),this)}),this)},defineClassElement:function(e,t){var r=t.descriptor;if("field"===t.kind){var i=t.initializer;r={enumerable:r.enumerable,writable:r.writable,configurable:r.configurable,value:void 0===i?void 0:i.call(e)}}Object.defineProperty(e,t.key,r)},decorateClass:function(e,t){var r=[],i=[],o={static:[],prototype:[],own:[]};if(e.forEach((function(e){this.addElementPlacement(e,o)}),this),e.forEach((function(e){if(!v(e))return r.push(e);var t=this.decorateElement(e,o);r.push(t.element),r.push.apply(r,t.extras),i.push.apply(i,t.finishers)}),this),!t)return{elements:r,finishers:i};var n=this.decorateConstructor(r,t);return i.push.apply(i,n.finishers),n.finishers=i,n},addElementPlacement:function(e,t,r){var i=t[e.placement];if(!r&&-1!==i.indexOf(e.key))throw new TypeError("Duplicated element ("+e.key+")");i.push(e.key)},decorateElement:function(e,t){for(var r=[],i=[],o=e.decorators,n=o.length-1;n>=0;n--){var a=t[e.placement];a.splice(a.indexOf(e.key),1);var s=this.fromElementDescriptor(e),c=this.toElementFinisherExtras((0,o[n])(s)||s);e=c.element,this.addElementPlacement(e,t),c.finisher&&i.push(c.finisher);var l=c.extras;if(l){for(var d=0;d<l.length;d++)this.addElementPlacement(l[d],t);r.push.apply(r,l)}}return{element:e,finishers:i,extras:r}},decorateConstructor:function(e,t){for(var r=[],i=t.length-1;i>=0;i--){var o=this.fromClassDescriptor(e),n=this.toClassDescriptor((0,t[i])(o)||o);if(void 0!==n.finisher&&r.push(n.finisher),void 0!==n.elements){e=n.elements;for(var a=0;a<e.length-1;a++)for(var s=a+1;s<e.length;s++)if(e[a].key===e[s].key&&e[a].placement===e[s].placement)throw new TypeError("Duplicated element ("+e[a].key+")")}}return{elements:e,finishers:r}},fromElementDescriptor:function(e){var t={kind:e.kind,key:e.key,placement:e.placement,descriptor:e.descriptor};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),"field"===e.kind&&(t.initializer=e.initializer),t},toElementDescriptors:function(e){var t;if(void 0!==e)return(t=e,function(e){if(Array.isArray(e))return e}(t)||function(e){if("undefined"!=typeof Symbol&&null!=e[Symbol.iterator]||null!=e["@@iterator"])return Array.from(e)}(t)||function(e,t){if(e){if("string"==typeof e)return w(e,t);var r=Object.prototype.toString.call(e).slice(8,-1);return"Object"===r&&e.constructor&&(r=e.constructor.name),"Map"===r||"Set"===r?Array.from(e):"Arguments"===r||/^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(r)?w(e,t):void 0}}(t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.")}()).map((function(e){var t=this.toElementDescriptor(e);return this.disallowProperty(e,"finisher","An element descriptor"),this.disallowProperty(e,"extras","An element descriptor"),t}),this)},toElementDescriptor:function(e){var t=String(e.kind);if("method"!==t&&"field"!==t)throw new TypeError('An element descriptor\'s .kind property must be either "method" or "field", but a decorator created an element descriptor with .kind "'+t+'"');var r=g(e.key),i=String(e.placement);if("static"!==i&&"prototype"!==i&&"own"!==i)throw new TypeError('An element descriptor\'s .placement property must be one of "static", "prototype" or "own", but a decorator created an element descriptor with .placement "'+i+'"');var o=e.descriptor;this.disallowProperty(e,"elements","An element descriptor");var n={kind:t,key:r,placement:i,descriptor:Object.assign({},o)};return"field"!==t?this.disallowProperty(e,"initializer","A method descriptor"):(this.disallowProperty(o,"get","The property descriptor of a field descriptor"),this.disallowProperty(o,"set","The property descriptor of a field descriptor"),this.disallowProperty(o,"value","The property descriptor of a field descriptor"),n.initializer=e.initializer),n},toElementFinisherExtras:function(e){return{element:this.toElementDescriptor(e),finisher:y(e,"finisher"),extras:this.toElementDescriptors(e.extras)}},fromClassDescriptor:function(e){var t={kind:"class",elements:e.map(this.fromElementDescriptor,this)};return Object.defineProperty(t,Symbol.toStringTag,{value:"Descriptor",configurable:!0}),t},toClassDescriptor:function(e){var t=String(e.kind);if("class"!==t)throw new TypeError('A class descriptor\'s .kind property must be "class", but a decorator created a class descriptor with .kind "'+t+'"');this.disallowProperty(e,"key","A class descriptor"),this.disallowProperty(e,"placement","A class descriptor"),this.disallowProperty(e,"descriptor","A class descriptor"),this.disallowProperty(e,"initializer","A class descriptor"),this.disallowProperty(e,"extras","A class descriptor");var r=y(e,"finisher");return{elements:this.toElementDescriptors(e.elements),finisher:r}},runClassFinishers:function(e,t){for(var r=0;r<t.length;r++){var i=(0,t[r])(e);if(void 0!==i){if("function"!=typeof i)throw new TypeError("Finishers must return a constructor.");e=i}}return e},disallowProperty:function(e,t,r){if(void 0!==e[t])throw new TypeError(r+" can't have a ."+t+" property.")}};return e}function m(e){var t,r=g(e.key);"method"===e.kind?t={value:e.value,writable:!0,configurable:!0,enumerable:!1}:"get"===e.kind?t={get:e.value,configurable:!0,enumerable:!1}:"set"===e.kind?t={set:e.value,configurable:!0,enumerable:!1}:"field"===e.kind&&(t={configurable:!0,writable:!0,enumerable:!0});var i={kind:"field"===e.kind?"field":"method",key:r,placement:e.static?"static":"field"===e.kind?"own":"prototype",descriptor:t};return e.decorators&&(i.decorators=e.decorators),"field"===e.kind&&(i.initializer=e.value),i}function k(e,t){void 0!==e.descriptor.get?t.descriptor.get=e.descriptor.get:t.descriptor.set=e.descriptor.set}function v(e){return e.decorators&&e.decorators.length}function b(e){return void 0!==e&&!(void 0===e.value&&void 0===e.writable)}function y(e,t){var r=e[t];if(void 0!==r&&"function"!=typeof r)throw new TypeError("Expected '"+t+"' to be a function");return r}function g(e){var t=function(e,t){if("object"!=typeof e||null===e)return e;var r=e[Symbol.toPrimitive];if(void 0!==r){var i=r.call(e,t||"default");if("object"!=typeof i)return i;throw new TypeError("@@toPrimitive must return a primitive value.")}return("string"===t?String:Number)(e)}(e,"string");return"symbol"==typeof t?t:String(t)}function w(e,t){(null==t||t>e.length)&&(t=e.length);for(var r=0,i=new Array(t);r<t;r++)i[r]=e[r];return i}function x(e,t,r){return x="undefined"!=typeof Reflect&&Reflect.get?Reflect.get:function(e,t,r){var i=function(e,t){for(;!Object.prototype.hasOwnProperty.call(e,t)&&null!==(e=_(e)););return e}(e,t);if(i){var o=Object.getOwnPropertyDescriptor(i,t);return o.get?o.get.call(r):o.value}},x(e,t,r||e)}function _(e){return _=Object.setPrototypeOf?Object.getPrototypeOf:function(e){return e.__proto__||Object.getPrototypeOf(e)},_(e)}let E;!function(e,t,r,i){var o=f();if(i)for(var n=0;n<i.length;n++)o=i[n](o);var a=t((function(e){o.initializeInstanceElements(e,s.elements)}),r),s=o.decorateClass(function(e){for(var t=[],r=function(e){return"method"===e.kind&&e.key===n.key&&e.placement===n.placement},i=0;i<e.length;i++){var o,n=e[i];if("method"===n.kind&&(o=t.find(r)))if(b(n.descriptor)||b(o.descriptor)){if(v(n)||v(o))throw new ReferenceError("Duplicated methods ("+n.key+") can't be decorated.");o.descriptor=n.descriptor}else{if(v(n)){if(v(o))throw new ReferenceError("Decorators can't be placed on different accessors with for the same property ("+n.key+").");o.decorators=n.decorators}k(n,o)}else t.push(n)}return t}(a.d.map(m)),e);o.initializeClassElements(a.F,s.elements),o.runClassFinishers(a.F,s.finishers)}([(0,o.M)("hui-shopping-list-card")],(function(e,t){class o extends t{constructor(...t){super(...t),e(this)}}return{F:o,d:[{kind:"method",static:!0,key:"getConfigElement",value:async function(){return await Promise.all([r.e(75009),r.e(78161),r.e(42955),r.e(69505),r.e(93098),r.e(32247)]).then(r.bind(r,92665)),document.createElement("hui-shopping-list-card-editor")}},{kind:"method",static:!0,key:"getStubConfig",value:function(){return{type:"shopping-list"}}},{kind:"field",decorators:[(0,n.C)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.S)()],key:"_config",value:void 0},{kind:"field",decorators:[(0,a.S)()],key:"_uncheckedItems",value:void 0},{kind:"field",decorators:[(0,a.S)()],key:"_checkedItems",value:void 0},{kind:"field",decorators:[(0,a.S)()],key:"_reordering",value:()=>!1},{kind:"field",decorators:[(0,a.S)()],key:"_renderEmptySortable",value:()=>!1},{kind:"field",key:"_sortable",value:void 0},{kind:"field",decorators:[(0,s.I)("#sortable")],key:"_sortableEl",value:void 0},{kind:"method",key:"getCardSize",value:function(){return 3+(this._config&&this._config.title?2:0)}},{kind:"method",key:"setConfig",value:function(e){this._config=e,this._uncheckedItems=[],this._checkedItems=[]}},{kind:"method",key:"hassSubscribe",value:function(){return this._fetchData(),[this.hass.connection.subscribeEvents((()=>this._fetchData()),"shopping_list_updated")]}},{kind:"method",key:"updated",value:function(e){if(x(_(o.prototype),"updated",this).call(this,e),!this._config||!this.hass)return;const t=e.get("hass"),r=e.get("_config");(e.has("hass")&&(null==t?void 0:t.themes)!==this.hass.themes||e.has("_config")&&(null==r?void 0:r.theme)!==this._config.theme)&&(0,h.R)(this,this.hass.themes,this._config.theme)}},{kind:"method",key:"render",value:function(){return this._config&&this.hass?i.dy`
      <ha-card
        .header=${this._config.title}
        class=${(0,c.$)({"has-header":"title"in this._config})}
      >
        <div class="addRow">
          <ha-svg-icon
            class="addButton"
            .path=${"M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z"}
            .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.add_item")}
            @click=${this._addItem}
          >
          </ha-svg-icon>
          <paper-input
            no-label-float
            class="addBox"
            placeholder=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.add_item")}
            @keydown=${this._addKeyPress}
          ></paper-input>
          <ha-svg-icon
            class="reorderButton"
            .path=${"M18 21L14 17H17V7H14L18 3L22 7H19V17H22M2 19V17H12V19M2 13V11H9V13M2 7V5H6V7H2Z"}
            .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.reorder_items")}
            @click=${this._toggleReorder}
          >
          </ha-svg-icon>
        </div>
        ${this._reordering?i.dy`
              <div id="sortable">
                ${(0,l.l)([this._uncheckedItems,this._renderEmptySortable],(()=>this._renderEmptySortable?"":this._renderItems(this._uncheckedItems)))}
              </div>
            `:this._renderItems(this._uncheckedItems)}
        ${this._checkedItems.length>0?i.dy`
              <div class="divider"></div>
              <div class="checked">
                <span>
                  ${this.hass.localize("ui.panel.lovelace.cards.shopping-list.checked_items")}
                </span>
                <ha-svg-icon
                  class="clearall"
                  tabindex="0"
                  .path=${"M5,13H19V11H5M3,17H17V15H3M7,7V9H21V7"}
                  .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.clear_items")}
                  @click=${this._clearItems}
                >
                </ha-svg-icon>
              </div>
              ${(0,d.r)(this._checkedItems,(e=>e.id),(e=>i.dy`
                    <div class="editRow">
                      <paper-checkbox
                        tabindex="0"
                        ?checked=${e.complete}
                        .itemId=${e.id}
                        @click=${this._completeItem}
                      ></paper-checkbox>
                      <paper-input
                        no-label-float
                        .value=${e.name}
                        .itemId=${e.id}
                        @change=${this._saveEdit}
                      ></paper-input>
                    </div>
                  `))}
            `:""}
      </ha-card>
    `:i.dy``}},{kind:"method",key:"_renderItems",value:function(e){return i.dy`
      ${(0,d.r)(e,(e=>e.id),(e=>i.dy`
            <div class="editRow" item-id=${e.id}>
              <paper-checkbox
                tabindex="0"
                ?checked=${e.complete}
                .itemId=${e.id}
                @click=${this._completeItem}
              ></paper-checkbox>
              <paper-input
                no-label-float
                .value=${e.name}
                .itemId=${e.id}
                @change=${this._saveEdit}
              ></paper-input>
              ${this._reordering?i.dy`
                    <ha-svg-icon
                      .title=${this.hass.localize("ui.panel.lovelace.cards.shopping-list.drag_and_drop")}
                      class="reorderButton"
                      .path=${"M7,19V17H9V19H7M11,19V17H13V19H11M15,19V17H17V19H15M7,15V13H9V15H7M11,15V13H13V15H11M15,15V13H17V15H15M7,11V9H9V11H7M11,11V9H13V11H11M15,11V9H17V11H15M7,7V5H9V7H7M11,7V5H13V7H11M15,7V5H17V7H15Z"}
                    >
                    </ha-svg-icon>
                  `:""}
            </div>
          `))}
    `}},{kind:"method",key:"_fetchData",value:async function(){if(!this.hass)return;const e=[],t=[],r=await(i=this.hass,i.callWS({type:"shopping_list/items"}));var i;for(const i in r)r[i].complete?e.push(r[i]):t.push(r[i]);this._checkedItems=e,this._uncheckedItems=t}},{kind:"method",key:"_completeItem",value:function(e){p(this.hass,e.target.itemId,{complete:e.target.checked}).catch((()=>this._fetchData()))}},{kind:"method",key:"_saveEdit",value:function(e){p(this.hass,e.target.itemId,{name:e.target.value}).catch((()=>this._fetchData())),e.target.blur()}},{kind:"method",key:"_clearItems",value:function(){var e;this.hass&&(e=this.hass,e.callWS({type:"shopping_list/items/clear"})).catch((()=>this._fetchData()))}},{kind:"get",key:"_newItem",value:function(){return this.shadowRoot.querySelector(".addBox")}},{kind:"method",key:"_addItem",value:function(e){const t=this._newItem;var r,i;t.value.length>0&&(r=this.hass,i=t.value,r.callWS({type:"shopping_list/items/add",name:i})).catch((()=>this._fetchData())),t.value="",e&&t.focus()}},{kind:"method",key:"_addKeyPress",value:function(e){13===e.keyCode&&this._addItem(null)}},{kind:"method",key:"_toggleReorder",value:async function(){if(!E){const e=await r.e(56087).then(r.bind(r,56087));E=e.Sortable}var e;(this._reordering=!this._reordering,await this.updateComplete,this._reordering)?this._createSortable():(null===(e=this._sortable)||void 0===e||e.destroy(),this._sortable=void 0)}},{kind:"method",key:"_createSortable",value:function(){const e=this._sortableEl;this._sortable=new E(e,{animation:150,fallbackClass:"sortable-fallback",dataIdAttr:"item-id",handle:"ha-svg-icon",onEnd:async t=>{var r,i;for(t.oldIndex!==t.newIndex&&((r=this.hass,i=this._sortable.toArray(),r.callWS({type:"shopping_list/items/reorder",item_ids:i})).catch((()=>this._fetchData())),this._uncheckedItems.splice(t.newIndex,0,this._uncheckedItems.splice(t.oldIndex,1)[0])),this._renderEmptySortable=!0,await this.updateComplete;null!=e&&e.lastElementChild;)e.removeChild(e.lastElementChild);this._renderEmptySortable=!1}})}},{kind:"get",static:!0,key:"styles",value:function(){return i.iv`
      ha-card {
        padding: 16px;
        height: 100%;
        box-sizing: border-box;
      }

      .has-header {
        padding-top: 0;
      }

      .editRow,
      .addRow,
      .checked {
        display: flex;
        flex-direction: row;
        align-items: center;
      }

      .addRow ha-icon {
        color: var(--secondary-text-color);
        --mdc-icon-size: 26px;
      }

      .addButton {
        padding-right: 16px;
        cursor: pointer;
      }

      .reorderButton {
        padding-left: 16px;
        cursor: pointer;
      }

      paper-checkbox {
        padding-left: 4px;
        padding-right: 20px;
        --paper-checkbox-label-spacing: 0px;
      }

      paper-input {
        flex-grow: 1;
      }

      .checked {
        margin: 12px 0;
        justify-content: space-between;
      }

      .checked span {
        color: var(--primary-text-color);
        font-weight: 500;
      }

      .divider {
        height: 1px;
        background-color: var(--divider-color);
        margin: 10px 0;
      }

      .clearall {
        cursor: pointer;
      }
    `}}]}}),(0,u.f)(i.oi))},1460:(e,t,r)=>{r.d(t,{l:()=>a});var i=r(15304),o=r(38941);const n={},a=(0,o.XM)(class extends o.Xe{constructor(){super(...arguments),this.ot=n}render(e,t){return t()}update(e,[t,r]){if(Array.isArray(t)){if(Array.isArray(this.ot)&&this.ot.length===t.length&&t.every(((e,t)=>e===this.ot[t])))return i.Jb}else if(this.ot===t)return i.Jb;return this.ot=Array.isArray(t)?Array.from(t):t,this.render(t,r)}})},86230:(e,t,r)=>{r.d(t,{r:()=>s});var i=r(15304),o=r(38941),n=r(81563);const a=(e,t,r)=>{const i=new Map;for(let o=t;o<=r;o++)i.set(e[o],o);return i},s=(0,o.XM)(class extends o.Xe{constructor(e){if(super(e),e.type!==o.pX.CHILD)throw Error("repeat() can only be used in text expressions")}dt(e,t,r){let i;void 0===r?r=t:void 0!==t&&(i=t);const o=[],n=[];let a=0;for(const t of e)o[a]=i?i(t,a):a,n[a]=r(t,a),a++;return{values:n,keys:o}}render(e,t,r){return this.dt(e,t,r).values}update(e,[t,r,o]){var s;const c=(0,n.i9)(e),{values:l,keys:d}=this.dt(t,r,o);if(!Array.isArray(c))return this.ct=d,l;const h=null!==(s=this.ct)&&void 0!==s?s:this.ct=[],p=[];let u,f,m=0,k=c.length-1,v=0,b=l.length-1;for(;m<=k&&v<=b;)if(null===c[m])m++;else if(null===c[k])k--;else if(h[m]===d[v])p[v]=(0,n.fk)(c[m],l[v]),m++,v++;else if(h[k]===d[b])p[b]=(0,n.fk)(c[k],l[b]),k--,b--;else if(h[m]===d[b])p[b]=(0,n.fk)(c[m],l[b]),(0,n._Y)(e,p[b+1],c[m]),m++,b--;else if(h[k]===d[v])p[v]=(0,n.fk)(c[k],l[v]),(0,n._Y)(e,c[m],c[k]),k--,v++;else if(void 0===u&&(u=a(d,v,b),f=a(h,m,k)),u.has(h[m]))if(u.has(h[k])){const t=f.get(d[v]),r=void 0!==t?c[t]:null;if(null===r){const t=(0,n._Y)(e,c[m]);(0,n.fk)(t,l[v]),p[v]=t}else p[v]=(0,n.fk)(r,l[v]),(0,n._Y)(e,c[m],r),c[t]=null;v++}else(0,n.ws)(c[k]),k--;else(0,n.ws)(c[m]),m++;for(;v<=b;){const t=(0,n._Y)(e,p[b+1]);(0,n.fk)(t,l[v]),p[v++]=t}for(;m<=k;){const e=c[m++];null!==e&&(0,n.ws)(e)}return this.ct=d,(0,n.hl)(e,p),i.Jb}})}}]);
//# sourceMappingURL=de84290e.js.map