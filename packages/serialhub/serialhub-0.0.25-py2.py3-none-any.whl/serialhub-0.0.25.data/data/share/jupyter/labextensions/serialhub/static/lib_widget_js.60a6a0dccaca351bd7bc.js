(self["webpackChunkserialhub"] = self["webpackChunkserialhub"] || []).push([["lib_widget_js"],{

/***/ "./lib/version.js":
/*!************************!*\
  !*** ./lib/version.js ***!
  \************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "MODULE_VERSION": () => (/* binding */ MODULE_VERSION),
/* harmony export */   "MODULE_NAME": () => (/* binding */ MODULE_NAME)
/* harmony export */ });
// Copyright (c) cdr4eelz
// Distributed under the terms of the Modified BSD License.
// eslint-disable-next-line @typescript-eslint/no-var-requires
const data = __webpack_require__(/*! ../package.json */ "./package.json");
/**
 * The _model_module_version/_view_module_version this package implements.
 *
 * The html widget manager assumes that this is the same as the npm package
 * version number.
 */
const MODULE_VERSION = data.version;
/*
 * The current package name.
 */
const MODULE_NAME = data.name;
//# sourceMappingURL=version.js.map

/***/ }),

/***/ "./lib/webseriallink.js":
/*!******************************!*\
  !*** ./lib/webseriallink.js ***!
  \******************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SerialHubPort": () => (/* binding */ SerialHubPort)
/* harmony export */ });
// Copyright (c) cdr4eelz
// Distributed under the terms of the Modified BSD License.
class SerialHubPort {
    constructor(oldSP) {
        if (oldSP) {
            oldSP.disconnect(); //Dispose of prior "port" if passed to us
        }
        this.port = null;
        //this.outputStream = null;
        //this.outputDone = null;
        this.writer = null;
        //this.inputStream = null;
        //this.inputDone = null;
        this.reader = null;
    }
    async connect() {
        const NAV = window.navigator;
        if (!NAV || !NAV.serial) {
            return;
        }
        if (this.port) {
            await this.disconnect();
        }
        const filter = { usbVendorId: 0x2047 }; // TI proper ; unused 0x0451 for "TUSB2046 Hub"
        const rawPort = await NAV.serial.requestPort({ filters: [filter] });
        if (!rawPort) {
            return;
        }
        this.port = rawPort;
        await this.port.open({ baudRate: 115200 });
        //const encoder = new TextEncoderStream();
        //this.outputDone = encoder.readable.pipeTo(this.port.writable);
        //this.outputStream = encoder.writable;
        this.writer = this.port.writable.getWriter();
        //const decoder = new TextDecoderStream();
        //this.inputDone = this.port.readable.pipeTo(decoder.writable);
        //this.inputStream = decoder.readable;
        //this.reader = this.inputStream.getReader();
        this.reader = this.port.readable.getReader();
        console.log('CONNECT: ', this);
        //Let cbConnect initiate this.readLoop(f);
    }
    async disconnect() {
        console.log('CLOSE: ', this);
        if (this.reader) {
            await this.reader.cancel();
            this.reader = null;
            //if (this.inputDone) await this.inputDone.catch(() => {});
            //this.inputDone = null;
        }
        if (this.writer) {
            this.writer.close();
            this.writer = null;
            //await this.outputStream.getWriter().close();
            //await this.outputDone;
            //this.outputStream = null;
            //this.outputDone = null;
        }
        if (this.port) {
            await this.port.close();
            this.port = null;
        }
    }
    writeToStream(data) {
        if (this.writer) {
            data.forEach(async (d) => {
                var _a;
                //Anonymous function is ASYNC so it can AWAIT the write() call below
                console.log('[WRITE]', d);
                await ((_a = this.writer) === null || _a === void 0 ? void 0 : _a.write(d)); // AWAIT in sequence, to avoid parallel promises
            });
        }
    }
    async readLoop(cbRead) {
        while (this.reader) {
            const { value, done } = await this.reader.read();
            if (value) {
                console.log('[readLoop] VALUE', value);
                cbRead(value);
            }
            if (done) {
                console.log('[readLoop] DONE', done);
                this.reader.releaseLock();
                break;
            }
        }
    }
    static isSupported() {
        const NAV = window.navigator;
        if (NAV === undefined || NAV === null) {
            return false;
        }
        const SER = NAV.serial;
        if (SER === undefined || SER === null) {
            return false;
        }
        return true;
    }
    static createHub(cbConnect) {
        const W = window;
        const oldSER = W.serPort;
        const SER = new SerialHubPort(oldSER);
        W.serPort = SER; //Assign to a global location
        SER.connect().then(() => {
            cbConnect(SER);
        });
        return SER;
    }
}
//# sourceMappingURL=webseriallink.js.map

/***/ }),

/***/ "./lib/widget.js":
/*!***********************!*\
  !*** ./lib/widget.js ***!
  \***********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "SerialHubModel": () => (/* binding */ SerialHubModel),
/* harmony export */   "SerialHubView": () => (/* binding */ SerialHubView)
/* harmony export */ });
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @jupyter-widgets/base */ "webpack/sharing/consume/default/@jupyter-widgets/base");
/* harmony import */ var _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _version__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./version */ "./lib/version.js");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../style/index.css */ "./style/index.css");
/* harmony import */ var _style_index_css__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_style_index_css__WEBPACK_IMPORTED_MODULE_1__);
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! @lumino/coreutils */ "webpack/sharing/consume/default/@lumino/coreutils");
/* harmony import */ var _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2___default = /*#__PURE__*/__webpack_require__.n(_lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__);
/* harmony import */ var _webseriallink__WEBPACK_IMPORTED_MODULE_4__ = __webpack_require__(/*! ./webseriallink */ "./lib/webseriallink.js");
// Copyright (c) cdr4eelz
// Distributed under the terms of the Modified BSD License.


// Import the CSS
 //was '../css/widget.css'



class SerialHubModel extends _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__.DOMWidgetModel {
    defaults() {
        return Object.assign(Object.assign({}, super.defaults()), { _model_name: SerialHubModel.model_name, _model_module: SerialHubModel.model_module, _model_module_version: SerialHubModel.model_module_version, _view_name: SerialHubModel.view_name, _view_module: SerialHubModel.view_module, _view_module_version: SerialHubModel.view_module_version, isSupported: false, status: 'Initializing...', value: 'Loading...', pkt_recv_front: 0, pkt_recv_back: 0, pkt_send_front: 0, pkt_send_back: 0 });
    }
    static get mytempid() {
        return SerialHubModel._mytempid;
    }
}
SerialHubModel._mytempid = _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__.uuid();
SerialHubModel.serializers = Object.assign({}, _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__.DOMWidgetModel.serializers
// Add any extra serializers here
);
SerialHubModel.model_name = 'SerialHubModel';
SerialHubModel.model_module = _version__WEBPACK_IMPORTED_MODULE_3__.MODULE_NAME;
SerialHubModel.model_module_version = _version__WEBPACK_IMPORTED_MODULE_3__.MODULE_VERSION;
SerialHubModel.view_name = 'SerialHubView'; // Set to null if no view
SerialHubModel.view_module = _version__WEBPACK_IMPORTED_MODULE_3__.MODULE_NAME; // Set to null if no view
SerialHubModel.view_module_version = _version__WEBPACK_IMPORTED_MODULE_3__.MODULE_VERSION;
class SerialHubView extends _jupyter_widgets_base__WEBPACK_IMPORTED_MODULE_0__.DOMWidgetView {
    constructor() {
        super(...arguments);
        this._el_status = null;
        this._el_stats = null;
        this._el_value = null;
        this._shp = null;
    }
    render() {
        this.el.id = this.id || _lumino_coreutils__WEBPACK_IMPORTED_MODULE_2__.UUID.uuid4();
        this.el.classList.add('xx-serialhub-widget');
        /* Create a couple sub-Elements for our custom widget */
        this._el_status = window.document.createElement('span');
        this._el_status.classList.add('xx-serialhub-status');
        this._el_stats = window.document.createElement('span');
        this._el_stats.classList.add('xx-serialhub-stats');
        this._el_value = window.document.createElement('pre');
        this._el_value.classList.add('xx-serialhub-value');
        /* Click events wrapped to capture "this" object */
        this._el_status.onclick = (ev) => this.click_status(ev);
        this._el_value.onclick = (ev) => this.click_value(ev);
        /* Maybe is more appropriate append() function availablie? */
        this.el.append(this._el_status, this._el_stats, this._el_value);
        this.changed_status();
        this.changed_value();
        this.changed_stats();
        this.model.on('change:status', this.changed_status, this);
        this.model.on('change:value', this.changed_value, this);
        this.model.on('change:pkt_recv_front', this.changed_stats, this);
        this.model.on('change:pkt_recv_back', this.changed_stats, this);
        this.model.on('change:pkt_send_front', this.changed_stats, this);
        this.model.on('change:pkt_send_back', this.changed_stats, this);
        this.model.on('msg:custom', this.msg_custom, this);
        this.model.set('isSupported', _webseriallink__WEBPACK_IMPORTED_MODULE_4__.SerialHubPort.isSupported());
        this.model.set('status', _webseriallink__WEBPACK_IMPORTED_MODULE_4__.SerialHubPort.isSupported() ? 'Supported' : 'Unsupported');
        this.touch();
        return this;
    }
    changed_status() {
        if (this._el_status && this.model) {
            this._el_status.textContent = this.model.get('status');
        }
    }
    changed_value() {
        if (this._el_value && this.model) {
            this._el_value.textContent = this.model.get('value');
        }
    }
    changed_stats() {
        if (this._el_stats) {
            let stats = '';
            stats += 'Rf:' + this.model.get('pkt_recv_front');
            stats += ' Rb:' + this.model.get('pkt_recv_back');
            stats += ' Sf:' + this.model.get('pkt_send_front');
            stats += ' Sb:' + this.model.get('pkt_send_back');
            this._el_stats.textContent = stats;
        }
    }
    click_status(ev) {
        console.log('click_status', this, this.model, ev);
        this._shp = _webseriallink__WEBPACK_IMPORTED_MODULE_4__.SerialHubPort.createHub((theSHP) => {
            console.log('theSHP', theSHP);
            theSHP.readLoop((value) => {
                console.log('DATA-IN', value);
                this.model.send({ type: 'RECV' }, {}, [value]);
                const cnt = this.model.get('pkt_recv_front') + 1;
                this.model.set('pkt_recv_front', cnt);
            });
        });
        console.log('DONE click', this._shp);
    }
    click_value(ev) {
        var _a;
        if (!this || !this.model) {
            return;
        }
        this.model.send({ type: 'text', text: 'VALUE-6\n' }, {}, []);
        const encoder = new TextEncoder();
        const theData = encoder.encode('6');
        (_a = this._shp) === null || _a === void 0 ? void 0 : _a.writeToStream([theData]);
        this.model.set('pkt_send_front', this.model.get('pkt_send_front') + 1);
    }
    msg_custom(mData, mBuffs) {
        var _a, _b;
        //console.log(this, mData, mBuffs);
        const msgType = mData['type'];
        if (msgType === 'SEND') {
            console.log('MSG-SEND', mBuffs);
            (_a = this._shp) === null || _a === void 0 ? void 0 : _a.writeToStream(mBuffs);
            this.model.set('pkt_send_front', this.model.get('pkt_send_front') + 1);
        }
        else if (msgType === 'SEND2') {
            const encoder = new TextEncoder();
            const theData = encoder.encode(mData['text']);
            (_b = this._shp) === null || _b === void 0 ? void 0 : _b.writeToStream([theData]);
            this.model.set('pkt_send_front', this.model.get('pkt_send_front') + 1);
        }
        else {
            console.log('UNKNOWN MESSAGE: ', msgType, mData, mBuffs);
        }
    }
}
//# sourceMappingURL=widget.js.map

/***/ }),

/***/ "./node_modules/css-loader/dist/cjs.js!./style/index.css":
/*!***************************************************************!*\
  !*** ./node_modules/css-loader/dist/cjs.js!./style/index.css ***!
  \***************************************************************/
/***/ ((module, exports, __webpack_require__) => {

// Imports
var ___CSS_LOADER_API_IMPORT___ = __webpack_require__(/*! ../node_modules/css-loader/dist/runtime/api.js */ "./node_modules/css-loader/dist/runtime/api.js");
var ___CSS_LOADER_AT_RULE_IMPORT_0___ = __webpack_require__(/*! -!../node_modules/css-loader/dist/cjs.js!./base.css */ "./node_modules/css-loader/dist/cjs.js!./style/base.css");
exports = ___CSS_LOADER_API_IMPORT___(false);
exports.i(___CSS_LOADER_AT_RULE_IMPORT_0___);
// Module
exports.push([module.id, "\n", ""]);
// Exports
module.exports = exports;


/***/ }),

/***/ "./style/index.css":
/*!*************************!*\
  !*** ./style/index.css ***!
  \*************************/
/***/ ((module, __unused_webpack_exports, __webpack_require__) => {

var api = __webpack_require__(/*! !../node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js */ "./node_modules/style-loader/dist/runtime/injectStylesIntoStyleTag.js");
            var content = __webpack_require__(/*! !!../node_modules/css-loader/dist/cjs.js!./index.css */ "./node_modules/css-loader/dist/cjs.js!./style/index.css");

            content = content.__esModule ? content.default : content;

            if (typeof content === 'string') {
              content = [[module.id, content, '']];
            }

var options = {};

options.insert = "head";
options.singleton = false;

var update = api(content, options);



module.exports = content.locals || {};

/***/ }),

/***/ "./package.json":
/*!**********************!*\
  !*** ./package.json ***!
  \**********************/
/***/ ((module) => {

"use strict";
module.exports = JSON.parse('{"name":"serialhub","version":"0.0.25","description":"WebSerial widget for Jupyter Hub/Lab","keywords":["jupyter","jupyterlab","jupyterlab-extension","widgets"],"homepage":"https://github.com/cdr4eelz/serialhub","bugs":{"url":"https://github.com/cdr4eelz/serialhub/issues"},"license":"BSD-3-Clause","author":{"name":"cdr4eelz","email":"1408777+cdr4eelz@users.noreply.github.com"},"files":["lib/**/*.{d.ts,eot,gif,html,jpg,js,js.map,json,png,svg,woff2,ttf}","style/**/*.{css,js,eot,gif,html,jpg,json,png,svg,woff2,ttf}","schema/*.json"],"main":"lib/index.js","types":"lib/index.d.ts","style":"style/index.css","repository":{"type":"git","url":"https://github.com/cdr4eelz/serialhub.git"},"scripts":{"build":"jlpm run build:lib && jlpm run build:labextension:dev","build:prod":"jlpm run clean && jlpm run build:lib && jlpm run build:labextension","build:labextension":"jupyter labextension build .","build:labextension:dev":"jupyter labextension build --development True .","build:lib":"tsc","build:nbextension":"webpack --node-env production","webpack:help":"webpack --help","webpack:version":"webpack -v","build:all":"jlpm run build:lib && jlpm run build:labextension:dev && jlpm run build:nbextension","clean":"jlpm run clean:lib","clean:lib":"rimraf lib tsconfig.tsbuildinfo","clean:labextension":"rimraf serialhub/labextension","clean:nbextension":"rimraf serialhub/nbextension/static/index.js","clean:all":"jlpm run clean:lib && jlpm run clean:labextension && jlpm run clean:nbextension","eslint":"eslint . --ext .ts,.tsx --fix","eslint:check":"eslint . --ext .ts,.tsx","install:extension":"jlpm run build","watch":"run-p watch:src watch:labextension","watch:src":"tsc -w","watch:labextension":"jupyter labextension watch ."},"dependencies":{"@jupyterlab/application":"^3.1.0","@jupyterlab/coreutils":"^5.1.0","@jupyterlab/services":"^6.1.0","@jupyter-widgets/base":"^2 || ^3 || ^4","@lumino/coreutils":"^1.5.3","@lumino/widgets":"^1.19.0","lodash":"^4.17.19","minimist":"^1.2.3"},"devDependencies":{"@jupyterlab/builder":"^3.1.0","@typescript-eslint/eslint-plugin":"^4.8.1","@typescript-eslint/parser":"^4.8.1","eslint":"^7.14.0","eslint-config-prettier":"^6.15.0","eslint-plugin-prettier":"^3.1.4","mkdirp":"^1.0.3","npm-run-all":"^4.1.5","prettier":"^2.1.1","rimraf":"^3.0.2","typescript":"~4.1.3","webpack":"^5","webpack-cli":"^4","source-map-loader":"^0.2.4","style-loader":"^1.0.0","ts-loader":"^9","css-loader":"^3.2.0"},"sideEffects":["style/*.css","style/index.js"],"styleModule":"style/index.js","publishConfig":{"access":"public"},"jupyterlab":{"sharedPackages":{"@jupyter-widgets/base":{"bundled":false,"singleton":true}},"discovery":{"server":{"managers":["pip"],"base":{"name":"serialhub"}}},"extension":"lib/plugin","outputDir":"serialhub/labextension"},"jupyter-releaser":{"hooks":{"before-build-npm":["python -m pip install jupyterlab~=3.1","jlpm"]}}}');

/***/ })

}]);
//# sourceMappingURL=lib_widget_js.60a6a0dccaca351bd7bc.js.map