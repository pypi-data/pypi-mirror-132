/**
 * Django Image Uploader Widget - An image uploader widget for django.
 * @version v0.1.0
 * @author Eduardo Oliveira (EduardoJM) <eduardo_y05@outlook.com>.
 * @link https://github.com/inventare/django-image-uploader-widget
 * 
 * Licensed under the MIT License (https://github.com/inventare/django-image-uploader-widget/blob/main/LICENSE).
 */

"use strict";

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } }

function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

var ImageUploaderWidget = /*#__PURE__*/function () {
  function ImageUploaderWidget(_element) {
    var _this = this;

    _classCallCheck(this, ImageUploaderWidget);

    _defineProperty(this, "element", void 0);

    _defineProperty(this, "fileInput", void 0);

    _defineProperty(this, "checkboxInput", void 0);

    _defineProperty(this, "emptyMarker", void 0);

    _defineProperty(this, "dropLabel", void 0);

    _defineProperty(this, "canDelete", false);

    _defineProperty(this, "dragging", false);

    _defineProperty(this, "id", void 0);

    _defineProperty(this, "raw", null);

    _defineProperty(this, "file", null);

    _defineProperty(this, "onEmptyMarkerClick", function () {
      _this.fileInput.click();
    });

    _defineProperty(this, "onDrop", function (e) {
      e.preventDefault();
      _this.dragging = false;

      _this.element.classList.remove('drop-zone');

      if (e.dataTransfer.files.length) {
        _this.fileInput.files = e.dataTransfer.files;
        _this.file = _this.fileInput.files[0];
        _this.raw = null;

        _this.renderWidget();
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
      if (e.relatedTarget && e.relatedTarget.closest('.iuw-root') === _this.element) {
        return;
      }

      _this.dragging = false;

      _this.element.classList.remove('drop-zone');
    });

    _defineProperty(this, "onImagePreviewClick", function (e) {
      if (e && e.target) {
        var targetElement = e.target;

        if (e && e.target && targetElement.closest('.iuw-delete-icon')) {
          var element = targetElement.closest('.iuw-image-preview');
          element.parentElement.removeChild(element);
          _this.checkboxInput.checked = true;
          _this.fileInput.value = null;
          _this.file = null;
          _this.raw = null;

          _this.renderWidget();

          return;
        }
      }

      _this.fileInput.click();
    });

    _defineProperty(this, "onFileInputChange", function () {
      if (_this.fileInput.files.length > 0) {
        _this.file = _this.fileInput.files[0];
      }

      _this.renderWidget();
    });

    this.element = _element;
    this.fileInput = _element.querySelector('input[type=file]');
    this.checkboxInput = _element.querySelector('input[type=checkbox]');
    this.emptyMarker = this.element.querySelector('.iuw-empty');
    this.canDelete = _element.getAttribute('data-candelete') === 'true';
    this.dragging = false;
    this.id = this.fileInput.getAttribute('id');
    this.dropLabel = this.element.querySelector('.drop-label');

    if (this.dropLabel) {
      this.dropLabel.setAttribute('for', this.id);
    } // add events


    this.fileInput.addEventListener('change', this.onFileInputChange);
    this.emptyMarker.addEventListener('click', this.onEmptyMarkerClick);
    this.element.addEventListener('dragenter', this.onDragEnter);
    this.element.addEventListener('dragover', this.onDragOver);
    this.element.addEventListener('dragleave', this.onDragLeave);
    this.element.addEventListener('dragend', this.onDragLeave);
    this.element.addEventListener('drop', this.onDrop); // init

    this.raw = _element.getAttribute('data-raw');
    this.file = null;
    this.renderWidget();
  }

  _createClass(ImageUploaderWidget, [{
    key: "renderPreview",
    value: function renderPreview(url) {
      var preview = document.createElement('div');
      preview.classList.add('iuw-image-preview');
      var img = document.createElement('img');
      img.src = url;
      preview.appendChild(img);

      if (this.canDelete) {
        var span = document.createElement('span');
        span.classList.add('iuw-delete-icon');
        span.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" width="100%" height="100%"><path xmlns="http://www.w3.org/2000/svg" d="m289.94 256 95-95A24 24 0 0 0 351 127l-95 95-95-95a24 24 0 0 0-34 34l95 95-95 95a24 24 0 1 0 34 34l95-95 95 95a24 24 0 0 0 34-34z"></path></svg>';
        preview.appendChild(span);
      }

      return preview;
    }
  }, {
    key: "renderWidget",
    value: function renderWidget() {
      var _this2 = this;

      if (!this.file && !this.raw) {
        this.element.classList.remove('non-empty');

        if (this.checkboxInput) {
          this.checkboxInput.checked = true;
        }
      } else {
        this.element.classList.add('non-empty');

        if (this.checkboxInput) {
          this.checkboxInput.checked = false;
        }
      }

      Array.from(this.element.querySelectorAll('.iuw-image-preview')).forEach(function (item) {
        return _this2.element.removeChild(item);
      });

      if (this.file) {
        var url = URL.createObjectURL(this.file);
        this.element.appendChild(this.renderPreview(url));
      }

      if (this.raw) {
        this.element.appendChild(this.renderPreview(this.raw));
      }

      Array.from(this.element.querySelectorAll('.iuw-image-preview')).forEach(function (item) {
        return item.addEventListener('click', _this2.onImagePreviewClick);
      });
    }
  }]);

  return ImageUploaderWidget;
}();

document.addEventListener('DOMContentLoaded', function () {
  Array.from(document.querySelectorAll('.iuw-root')).map(function (element) {
    return new ImageUploaderWidget(element);
  });

  if (window && window.django && window.django.jQuery) {
    var $ = window.django.jQuery;
    $(document).on('formset:added', function (_, row) {
      if (!row.length) {
        return;
      }

      Array.from(row[0].querySelectorAll('.iuw-root')).map(function (element) {
        return new ImageUploaderWidget(element);
      });
    });
  }
}); // export for testing