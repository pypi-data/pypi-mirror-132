/**
 * Django Image Uploader Widget - An image uploader widget for django.
 * @version v0.1.0
 * @author Eduardo Oliveira (EduardoJM) <eduardo_y05@outlook.com>.
 * @link https://github.com/inventare/django-image-uploader-widget
 * 
 * Licensed under the MIT License (https://github.com/inventare/django-image-uploader-widget/blob/main/LICENSE).
 */

"use strict";

function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }

function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }

function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) { arr2[i] = arr[i]; } return arr2; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var ImageUploaderInline = /*#__PURE__*/function () {
  function ImageUploaderInline(element) {
    var _this = this;

    _classCallCheck(this, ImageUploaderInline);

    _defineProperty(this, "element", void 0);

    _defineProperty(this, "inlineGroup", void 0);

    _defineProperty(this, "inlineFormset", void 0);

    _defineProperty(this, "tempFileInput", null);

    _defineProperty(this, "next", 0);

    _defineProperty(this, "dragging", false);

    _defineProperty(this, "onDrop", function (e) {
      e.preventDefault();
      _this.dragging = false;

      _this.element.classList.remove('drop-zone');

      if (e.dataTransfer.files.length) {
        var _iterator = _createForOfIteratorHelper(e.dataTransfer.files),
            _step;

        try {
          for (_iterator.s(); !(_step = _iterator.n()).done;) {
            var file = _step.value;

            _this.addFile(file);
          }
        } catch (err) {
          _iterator.e(err);
        } finally {
          _iterator.f();
        }
      }
    });

    _defineProperty(this, "onDragEnter", function () {
      _this.dragging = true;

      _this.element.classList.add('drop-zone');
    });

    _defineProperty(this, "onDragOver", function (e) {
      if (e) {
        e.preventDefault();
      }
    });

    _defineProperty(this, "onDragLeave", function (e) {
      if (e.relatedTarget && e.relatedTarget.closest('.iuw-inline-root') === _this.element) {
        return;
      }

      _this.dragging = false;

      _this.element.classList.remove('drop-zone');
    });

    _defineProperty(this, "onRelatedItemClick", function (e) {
      if (!e || !e.target) {
        return;
      }

      var target = e.target;
      var item = target.closest('.inline-related');

      if (target.closest('.iuw-delete-icon')) {
        if (item.getAttribute('data-raw')) {
          item.classList.add('deleted');
          var checkboxInput = item.querySelector('input[type=checkbox]');
          checkboxInput.checked = true;
        } else {
          item.parentElement.removeChild(item);
        }

        _this.updateEmpty();

        return;
      }

      var fileInput = item.querySelector('input[type=file]');

      if (e.target === fileInput) {
        return;
      }

      fileInput.click();
    });

    _defineProperty(this, "onFileInputChange", function (e) {
      var target = e.target;

      if (target.tagName !== 'INPUT') {
        return;
      }

      var fileInput = target;
      var files = fileInput.files;

      if (files.length <= 0) {
        return;
      }

      var imgTag = target.closest('.inline-related').querySelector('img');

      if (imgTag) {
        imgTag.src = URL.createObjectURL(files[0]);
      }
    });

    _defineProperty(this, "onTempFileChange", function () {
      var filesList = _this.tempFileInput.files;

      if (filesList.length <= 0) {
        return;
      }

      _this.tempFileInput.removeEventListener('change', _this.onTempFileChange);

      _this.tempFileInput.parentElement.removeChild(_this.tempFileInput);

      _this.tempFileInput = null;

      _this.addFile(filesList[0]);
    });

    _defineProperty(this, "onChooseAddImageAreaClick", function () {
      if (!_this.tempFileInput) {
        _this.tempFileInput = document.createElement('input');

        _this.tempFileInput.setAttribute('type', 'file');

        _this.tempFileInput.classList.add('temp_file');

        _this.tempFileInput.setAttribute('accept', 'image/*');

        _this.tempFileInput.style.display = 'none';

        _this.tempFileInput.addEventListener('change', _this.onTempFileChange);

        _this.element.appendChild(_this.tempFileInput);
      }

      _this.tempFileInput.click();
    });

    this.element = element;
    this.inlineGroup = element.closest('.inline-group');
    this.inlineFormset = JSON.parse(this.inlineGroup.getAttribute('data-inline-formset'));
    this.updateEmpty();
    this.updateAllIndexes();
    Array.from(this.element.querySelectorAll('.inline-related')).forEach(function (item) {
      return _this.adjustInlineRelated(item);
    });
    Array.from(this.element.querySelectorAll('.iuw-add-image-btn, .iuw-empty')).forEach(function (item) {
      return item.addEventListener('click', _this.onChooseAddImageAreaClick);
    });
    this.element.addEventListener('dragenter', this.onDragEnter);
    this.element.addEventListener('dragover', this.onDragOver);
    this.element.addEventListener('dragleave', this.onDragLeave);
    this.element.addEventListener('dragend', this.onDragLeave);
    this.element.addEventListener('drop', this.onDrop);
  }

  _createClass(ImageUploaderInline, [{
    key: "updateEmpty",
    value: function updateEmpty() {
      var _this$element$querySe = this.element.querySelectorAll('.inline-related:not(.empty-form):not(.deleted)'),
          length = _this$element$querySe.length;

      if (length > 0) {
        this.element.classList.add('non-empty');
      } else {
        this.element.classList.remove('non-empty');
      }
    }
  }, {
    key: "updateElementIndex",
    value: function updateElementIndex(element, prefix, index) {
      var id_regex = new RegExp("(".concat(prefix, "-(\\d+|__prefix__))"));
      var replacement = "".concat(prefix, "-").concat(index);

      if (element.getAttribute('for')) {
        element.setAttribute('for', element.getAttribute('for').replace(id_regex, replacement));
      }

      if (element.id) {
        element.id = element.id.replace(id_regex, replacement);
      }

      if (element.getAttribute('name')) {
        element.setAttribute('name', element.getAttribute('name').replace(id_regex, replacement));
      }
    }
  }, {
    key: "updateAllIndexes",
    value: function updateAllIndexes() {
      var _this2 = this;

      var prefix = this.inlineFormset.options.prefix;

      var _Array$from$map$map = Array.from(this.element.querySelectorAll('.inline-related:not(.empty-form)')).map(function (item) {
        return item;
      }).map(function (item, index) {
        _this2.updateElementIndex(item, prefix, index);

        Array.from(item.querySelectorAll('*')).map(function (childItem) {
          return childItem;
        }).forEach(function (childItem) {
          _this2.updateElementIndex(childItem, prefix, index);
        });
        return item;
      }),
          count = _Array$from$map$map.length;

      this.next = count;
      var totalFormsInput = document.getElementById("id_".concat(prefix, "-TOTAL_FORMS"));
      totalFormsInput.value = String(this.next);
      var maxFormsInput = document.getElementById("id_".concat(prefix, "-MAX_NUM_FORMS"));
      var maxNumber = parseInt(maxFormsInput.value, 10);

      if (Number.isNaN(maxNumber)) {
        maxNumber = 0;
      }

      if (maxFormsInput.value === '' || maxNumber - this.next > 0) {
        this.element.querySelector('.iuw-add-image-btn').classList.add('visible-by-number');
      } else {
        this.element.querySelector('.iuw-add-image-btn').classList.remove('visible-by-number');
      }
    }
  }, {
    key: "adjustInlineRelated",
    value: function adjustInlineRelated(element) {
      var inputs = Array.from(element.querySelectorAll('input[type=hidden], input[type=checkbox], input[type=file]')).map(function (item) {
        item.parentElement.removeChild(item);
        return item;
      }); // get raw image url

      var rawImage = document.querySelector('p.file-upload a');

      if (element.classList.contains('empty-form')) {
        rawImage = null;
      }

      if (rawImage) {
        element.setAttribute('data-raw', rawImage.getAttribute('href'));
      } // clear element


      element.innerHTML = '';
      inputs.forEach(function (item) {
        return element.appendChild(item);
      }); // apply raw image

      if (rawImage) {
        this.appendItem(element, rawImage.getAttribute('href'));
      }
    }
  }, {
    key: "appendItem",
    value: function appendItem(element, url) {
      var delete_icon = null;
      var related = element.closest('.inline-related');

      if (related.getAttribute('data-candelete') === 'true') {
        delete_icon = document.createElement('span');
        delete_icon.classList.add('iuw-delete-icon');
        delete_icon.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" width="100%" height="100%"><path xmlns="http://www.w3.org/2000/svg" d="m289.94 256 95-95A24 24 0 0 0 351 127l-95 95-95-95a24 24 0 0 0-34 34l95 95-95 95a24 24 0 1 0 34 34l95-95 95 95a24 24 0 0 0 34-34z"></path></svg>';
      }

      var img = document.createElement('img');
      img.src = url;
      element.appendChild(img);

      if (delete_icon) {
        element.appendChild(delete_icon);
      }

      related.removeEventListener('click', this.onRelatedItemClick);
      related.addEventListener('click', this.onRelatedItemClick);
      var fileInput = related.querySelector('input[type=file]');
      fileInput.removeEventListener('change', this.onFileInputChange);
      fileInput.addEventListener('change', this.onFileInputChange);
    }
  }, {
    key: "addFile",
    value: function addFile(file) {
      var template = this.element.querySelector('.inline-related.empty-form');

      if (!template) {
        return;
      }

      var row = template.cloneNode(true);
      row.classList.remove('empty-form');
      row.classList.remove('last-related');
      row.setAttribute('data-candelete', 'true');
      row.id = "".concat(this.inlineFormset.options.prefix, "-").concat(this.next);
      template.parentElement.insertBefore(row, template);
      var dataTransferList = new DataTransfer();
      dataTransferList.items.add(file);
      var rowFileInput = row.querySelector('input[type=file]');
      rowFileInput.files = dataTransferList.files;
      this.appendItem(row, URL.createObjectURL(file));
      this.updateEmpty();
      this.updateAllIndexes();
    }
  }]);

  return ImageUploaderInline;
}();

document.addEventListener('DOMContentLoaded', function () {
  Array.from(document.querySelectorAll('.iuw-inline-root')).map(function (element) {
    return new ImageUploaderInline(element);
  });
}); // export for testing