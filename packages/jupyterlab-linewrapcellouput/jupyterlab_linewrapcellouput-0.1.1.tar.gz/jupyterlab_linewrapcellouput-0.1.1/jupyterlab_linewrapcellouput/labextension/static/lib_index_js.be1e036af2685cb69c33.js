"use strict";
(self["webpackChunkjupyterlab_linewrapcellouput"] = self["webpackChunkjupyterlab_linewrapcellouput"] || []).push([["lib_index_js"],{

/***/ "./lib/index.js":
/*!**********************!*\
  !*** ./lib/index.js ***!
  \**********************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   "ButtonLineWrapCellOutput": () => (/* binding */ ButtonLineWrapCellOutput),
/* harmony export */   "default": () => (__WEBPACK_DEFAULT_EXPORT__)
/* harmony export */ });
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @lumino/disposable */ "webpack/sharing/consume/default/@lumino/disposable");
/* harmony import */ var _lumino_disposable__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_lumino_disposable__WEBPACK_IMPORTED_MODULE_0__);
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @jupyterlab/apputils */ "webpack/sharing/consume/default/@jupyterlab/apputils");
/* harmony import */ var _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1___default = /*#__PURE__*/__webpack_require__.n(_jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__);


function JupyterLabLineWrapCellOuputOn() {
    var divs = document.querySelectorAll(".jp-OutputArea-output pre");
    for (let i = 0; i < divs.length; i++) {
        var div = divs[i];
        if (div.style['whiteSpace'] != "pre")
            div.style["whiteSpace"] = "pre";
    }
}
function JupyterLabLineWrapCellOuputOff() {
    var divs = document.querySelectorAll(".jp-OutputArea-output pre");
    for (let i = 0; i < divs.length; i++) {
        var div = divs[i];
        if (div.style['whiteSpace'] != "pre-wrap")
            div.style["whiteSpace"] = "pre-wrap";
    }
}
/**
 * Initialization data for the jupyterlab_linewrapcelloutput extension.
 */
const plugin = {
    id: 'jupyterlab_linewrapcelloutput:plugin',
    autoStart: true,
    activate: (app) => {
        console.log('JupyterLab extension jupyterlab_linewrapcelloutput is activated!');
        app.docRegistry.addWidgetExtension('Notebook', new ButtonLineWrapCellOutput());
    }
};
class ButtonLineWrapCellOutput {
    createNew(panel, context) {
        const triggerLineWrapCellOutput = () => {
            if (SET) {
                SET = false;
                console.log('Extension jupyterlab_linewrapcelloutput disabled');
                clearInterval(t);
                JupyterLabLineWrapCellOuputOff();
                if (button.hasClass('selected'))
                    button.removeClass('selected');
            }
            else {
                SET = true;
                console.log('Extension jupyterlab_linewrapcelloutput enabled');
                t = setInterval(JupyterLabLineWrapCellOuputOn, 10);
                button.addClass('selected');
            }
        };
        const button = new _jupyterlab_apputils__WEBPACK_IMPORTED_MODULE_1__.ToolbarButton({
            className: 'buttonLineWrapCellOuput',
            iconClass: 'wll-WrapIcon',
            label: 'wrap',
            onClick: triggerLineWrapCellOutput,
            tooltip: 'Line Wrap Cell Ouput'
        });
        panel.toolbar.insertItem(10, 'LineWrapCellOutput', button);
        var SET = true;
        var t = setInterval(JupyterLabLineWrapCellOuputOn, 10);
        button.addClass('selected');
        return new _lumino_disposable__WEBPACK_IMPORTED_MODULE_0__.DisposableDelegate(() => { button.dispose(); });
    }
}
/* harmony default export */ const __WEBPACK_DEFAULT_EXPORT__ = (plugin);


/***/ })

}]);
//# sourceMappingURL=lib_index_js.be1e036af2685cb69c33.js.map