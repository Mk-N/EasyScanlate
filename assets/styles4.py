IMPORT_EXPORT_STYLES = """
    QDialog {
        background-color: #2B2B2B;
        color: #FFFFFF;
    }
    QGroupBox {
        font-weight: bold;
        border: 2px solid #555;
        border-radius: 5px;
        margin-top: 10px;
        padding-top: 10px;
        background-color: #333;
    }
    QGroupBox::title {
        subcontrol-origin: margin;
        left: 10px;
        padding: 0 5px;
    }
    QLabel {
        color: #FFFFFF;
    }
    QPushButton {
        background-color: #4A4A4A;
        color: #FFFFFF;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 6px 12px;
        min-width: 80px;
    }
    QPushButton:hover {
        background-color: #5A5A5A;
    }
    QPushButton:pressed {
        background-color: #3A3A3A;
    }
    QComboBox {
        background-color: #3A3A3A;
        color: #FFFFFF;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 4px 8px;
        min-width: 150px;
    }
    QComboBox:hover {
        background-color: #4A4A4A;
    }
    QComboBox::drop-down {
        border: none;
    }
    QComboBox QAbstractItemView {
        background-color: #3A3A3A;
        color: #FFFFFF;
        selection-background-color: #5A5A5A;
    }
    QRadioButton {
        color: #FFFFFF;
        spacing: 5px;
    }
    QRadioButton::indicator {
        width: 16px;
        height: 16px;
        border-radius: 8px;
        border: 2px solid #555;
        background-color: #2B2B2B;
    }
    QRadioButton::indicator:checked {
        background-color: #4A9EFF;
        border-color: #4A9EFF;
    }
    QCheckBox {
        color: #FFFFFF;
        spacing: 5px;
    }
    QCheckBox::indicator {
        width: 16px;
        height: 16px;
        border: 2px solid #555;
        border-radius: 3px;
        background-color: #2B2B2B;
    }
    QCheckBox::indicator:checked {
        background-color: #4A9EFF;
        border-color: #4A9EFF;
    }
    QLineEdit {
        background-color: #3A3A3A;
        color: #FFFFFF;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 4px 8px;
    }
    QLineEdit:focus {
        border-color: #4A9EFF;
    }
    QSpinBox {
        background-color: #3A3A3A;
        color: #FFFFFF;
        border: 1px solid #555;
        border-radius: 4px;
        padding: 4px 8px;
    }
"""

