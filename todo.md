# what i need

## done (milestone 0.2.1 release)

  #### addition
  - custom error msg box
    - link to github issue report if any error
  - dedicated import/export dialogs for OCR/translation data

  #### fixes
  - fix import/export OCR/translation data functionality

  #### modification
  - 

## currently in progress
  - fix find and replace bugs :
    - roman character not working for some reason if there are other profile in other type of character (non roman)
    - profile creation/switching crashes the app when on find

## not yet started

  #### addition
  - add manual textbox insertion
  - implement watermarking
  - textbox styles
    - add stroke to typography
    - add directional blur to typography
    - add drop shadow to both
    - add 
  - add issue template for crash reports
  - 2 pane view of manhwa (for original and translated view side by side)(layers and overlays can be individualy toggle off and on)
  - add tool bar on the right
  - add direct retranslate on main window
  - add more items for ocr export
    - ocr tagging
    - pdf
    - docs
  - add window pos and size saves (remember from last session)
  - theme 
    - light mode
    - contrast
    - background gradient
  - split ocr result
  - add z index and reordering of textbox on the same img

  #### fixes
  - fix skew/free transform

  #### modification
  - rework how gradient work
  - implement titlebar to all apps
  - save edited state of textboxitem
  - dynamic link between import export ocr and translation
  - change how translation Work
    - integrate it into main window
      - easier retranslate workflow
    - characters, places, and lore name dictionaries
  - hide textboximage button
  - profile improvement:
      - manual creation, deletion, rename
      - two pane view
  - make it possible to edit straight from textbox
  - advanced inpaint
    - free form selection (pen tools/draw)
    - switch on/off from selection
    - undo/redo
  - make font to be from system
  - deprecate result widgets and table (be replaced by direct text editing on image textbox)
    - it should be merged into translation feature cause it still needed there
  - briefly highlight sync ocr
  - enhance ocr result merging