

- Let's go with ckeditor and improve to handle file uploads.  Current pull
  requests for managing files other than images.

  - https://github.com/django-ckeditor/django-ckeditor/pull/17

  - https://github.com/django-ckeditor/django-ckeditor/pull/153

  We also need to find a way to use the image picker for our icon field.









https://www.froala.com/wysiwyg-editor/#inline-demo

http://imperavi.com/redactor/
https://github.com/douglasmiranda/django-wysiwyg-redactor/
(paid)

https://github.com/summernote/summernote
https://github.com/summernote/django-summernote
(uses bootstrap)


ckeditor




Setup imaging.

$ sudo apt-get install python-dev 
$ sudo apt-get install python-pil
$ pip install pillow






Looks like ckeditor has scope for different
file and image browsers.  (or at least used to).

    http://docs.cksource.com/CKEditor_3.x/Developers_Guide/File_Browser_%28Uploader%29

    http://docs.ckeditor.com/#!/api/CKEDITOR.config-cfg-skin


    filebrowserWindowWidth : '640',
            filebrowserWindowHeight : '480'
     "filebrowserUploadUrl": "/ckeditor/upload/"
     "filebrowserBrowseUrl": "/ckeditor/browse/"


     filebrowserFlashBrowseUrl : String



     http://203.28.246.145:9000/ckeditor/browse/
     http://203.28.246.145:9000/ckeditor/upload/



<div class="django-ckeditor-widget" data-field-id="id_description" style="display: inline-block;">
<textarea cols="40" id="id_description" name="description" rows="10"
data-processed="0" data-config='{"filebrowserWindowWidth": 940,
"toolbar_Basic": [["Source", "-", "Bold", "Italic"]], "language": "en-us",
"toolbar_Full": [["Styles", "Format", "Bold", "Italic", "Underline", "Strike",
"SpellChecker", "Undo", "Redo"], ["Link", "Unlink", "Anchor"], ["Image",
"Flash", "Table", "HorizontalRule"], ["TextColor", "BGColor"], ["Smiley",
"SpecialChar"], ["Source"]], "filebrowserUploadUrl": "/ckeditor/upload/",
"height": 291, "width": 835, "filebrowserBrowseUrl": "/ckeditor/browse/",
"skin": "moono", "filebrowserWindowHeight": 725, "toolbar": [["Format", "Bold",
"Italic", "Underline", "Strike", "SpellChecker"], ["NumberedList",
"BulletedList", "Indent", "Outdent", "JustifyLeft", "JustifyCenter",
"JustifyRight", "JustifyBlock"], ["Image", "Table", "Link", "Unlink", "Anchor",
"SectionLink", "Subscript", "Superscript"], ["Undo", "Redo"], ["Source"],
["Maximize"]]}' data-external-plugin-resources='[]' data-id="id_description"
data-type="ckeditortype">&lt;p&gt;Amazing Test service.&lt;/p&gt;




</textarea>
</div>
