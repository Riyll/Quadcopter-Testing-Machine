import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QFileDialog, QDialog, QFormLayout, QLabel, QLineEdit, QPushButton, QDialogButtonBox
import pandas as pd
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt



class Variables(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        variable_tab = QWidget()
        variable_layout = QVBoxLayout()

        p_button = QPushButton("Set P Values")
        p_button.clicked.connect(self.set_p_values)
        variable_layout.addWidget(p_button)

        a_button = QPushButton("Set A Values")
        a_button.clicked.connect(self.set_a_values)
        variable_layout.addWidget(a_button)

        v_button = QPushButton("Set V Values")
        v_button.clicked.connect(self.set_v_values)
        variable_layout.addWidget(v_button)

        theta_button = QPushButton("Set Theta Values")
        theta_button.clicked.connect(self.set_theta_values)
        variable_layout.addWidget(theta_button)

        variable_tab.setLayout(variable_layout)
        self.tab_widget.addTab(variable_tab, "Variables")

        self.setLayout(layout)

        # Define attributes for p values
        self.px_min_edit = None
        self.px_max_edit = None
        self.py_min_edit = None
        self.py_max_edit = None
        self.pz_min_edit = None
        self.pz_max_edit = None
        # Define attributes for a values
        self.ax_min_edit = None
        self.ax_max_edit = None
        self.ay_min_edit = None
        self.ay_max_edit = None
        self.az_min_edit = None
        self.az_max_edit = None
         # Define attributes for v values
        self.vx_min_edit = None
        self.vx_max_edit = None
        self.vy_min_edit = None
        self.vy_max_edit = None
        self.vz_min_edit = None
        self.vz_max_edit = None
        # Define attributes for theta values
        self.theta_x_min_edit = None
        self.theta_x_max_edit = None
        self.theta_y_min_edit = None
        self.theta_y_max_edit = None


        

    def set_p_values(self):
        self.p_values_window = QDialog(self)
        self.p_values_window.setWindowTitle("Set P Values")

        self.form_layout = QFormLayout(self.p_values_window)

        self.p_x_edit = QLineEdit()
        self.form_layout.addRow("Px Min:", self.p_x_edit)

        self.p_y_edit = QLineEdit()
        self.form_layout.addRow("Py Min:", self.p_y_edit)

        self.p_z_edit = QLineEdit()
        self.form_layout.addRow("Pz Min:", self.p_z_edit)

        self.p_x_edit2 = QLineEdit()
        self.form_layout.addRow("Px Max:", self.p_x_edit2)

        self.p_y_edit2 = QLineEdit()
        self.form_layout.addRow("Py Max:", self.p_y_edit2)

        self.p_z_edit2 = QLineEdit()
        self.form_layout.addRow("Pz Max:", self.p_z_edit2)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self.p_values_window)
        button_box.accepted.connect(self.save_p_values)
        button_box.rejected.connect(self.p_values_window.reject)

        self.form_layout.addRow(button_box)

        self.p_values_window.exec_()


    def save_p_values(self):
        px_min = self.p_x_edit.text()
        px_max = self.p_x_edit2.text()

        py_min = self.p_y_edit.text()
        py_max = self.p_y_edit2.text()

        pz_min = self.p_z_edit.text()
        pz_max = self.p_z_edit2.text()

        print("P Values: Px={}, Py={}, Pz={}".format((px_min, px_max), (py_min, py_max), (pz_min, pz_max)))

        self.p_values_window.accept()



    def set_a_values(self):
        self.a_values_window = QDialog(self)
        self.a_values_window.setWindowTitle("Set A Values")

        form_layout = QFormLayout(self.a_values_window)

        self.a_x_min_edit = QLineEdit()
        form_layout.addRow("Ax Min:", self.a_x_min_edit)

        self.a_y_min_edit = QLineEdit()
        form_layout.addRow("Ay Min:", self.a_y_min_edit)

        self.a_z_min_edit = QLineEdit()
        form_layout.addRow("Az Min:", self.a_z_min_edit)

        self.a_x_max_edit = QLineEdit()
        form_layout.addRow("Ax Max:", self.a_x_max_edit)

        self.a_y_max_edit = QLineEdit()
        form_layout.addRow("Ay Max:", self.a_y_max_edit)

        self.a_z_max_edit = QLineEdit()
        form_layout.addRow("Az Max:", self.a_z_max_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self.a_values_window)
        button_box.accepted.connect(self.save_a_values)
        button_box.rejected.connect(self.a_values_window.reject)

        form_layout.addRow(button_box)

        self.a_values_window.exec_()

    def save_a_values(self):
        ax_min = self.a_x_min_edit.text()
        ax_max = self.a_x_max_edit.text()

        ay_min = self.a_y_min_edit.text()
        ay_max = self.a_y_max_edit.text()

        az_min = self.a_z_min_edit.text()
        az_max = self.a_z_max_edit.text()

        print("A Values: Ax=({}, {}), Ay=({}, {}), Az=({}, {})".format(ax_min, ax_max, ay_min, ay_max, az_min, az_max))

        self.a_values_window.accept()


    def set_v_values(self):
        self.v_values_window = QDialog(self)
        self.v_values_window.setWindowTitle("Set V Values")

        form_layout = QFormLayout(self.v_values_window)

        self.vx_min_edit = QLineEdit()
        form_layout.addRow("Vx Min:", self.vx_min_edit)

        self.vy_min_edit = QLineEdit()
        form_layout.addRow("Vy Min:", self.vy_min_edit)

        self.vz_min_edit = QLineEdit()
        form_layout.addRow("Vz Min:", self.vz_min_edit)

        self.vx_max_edit = QLineEdit()
        form_layout.addRow("Vx Max:", self.vx_max_edit)

        self.vy_max_edit = QLineEdit()
        form_layout.addRow("Vy Max:", self.vy_max_edit)

        self.vz_max_edit = QLineEdit()
        form_layout.addRow("Vz Max:", self.vz_max_edit)

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self.v_values_window)
        button_box.accepted.connect(self.save_v_values)
        button_box.rejected.connect(self.v_values_window.reject)

        form_layout.addRow(button_box)

        self.v_values_window.exec_()

    def save_v_values(self):
        vx_min = self.vx_min_edit.text()
        vx_max = self.vx_max_edit.text()

        vy_min = self.vy_min_edit.text()
        vy_max = self.vy_max_edit.text()

        vz_min = self.vz_min_edit.text()
        vz_max = self.vz_max_edit.text()

        print("V Values: Vx=({},{}) Vy=({},{}) Vz=({},{})".format(vx_min, vx_max, vy_min, vy_max, vz_min, vz_max))

        self.v_values_window.accept()


    def set_theta_values(self):
        self.theta_values_window = QDialog(self)
        self.theta_values_window.setWindowTitle("Set Theta Values")

        form_layout = QFormLayout(self.theta_values_window)

        self.thetax_min_edit = QLineEdit()
        form_layout.addRow("Theta_x Min:", self.thetax_min_edit)

        self.thetay_min_edit = QLineEdit()
        form_layout.addRow("Theta_y Min:", self.thetay_min_edit)

        

        self.thetax_max_edit = QLineEdit()
        form_layout.addRow("Theta_x Max:", self.thetax_max_edit)

        self.thetay_max_edit = QLineEdit()
        form_layout.addRow("Theta_y Max:", self.thetay_max_edit)

       
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self.theta_values_window)
        button_box.accepted.connect(self.save_theta_values)
        button_box.rejected.connect(self.theta_values_window.reject)

        form_layout.addRow(button_box)

        self.theta_values_window.exec_()


    def save_theta_values(self):
        thetax_min = self.thetax_min_edit.text()
        thetax_max = self.thetax_max_edit.text()

        thetay_min = self.thetay_min_edit.text()
        thetay_max = self.thetay_max_edit.text()

        print("Theta Values: Theta_x=({},{}) Theta_y=({},{})".format(thetax_min, thetax_max, thetay_min, thetay_max))

        self.theta_values_window.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.variables_tab = Variables()
        

        self.tabs = QTabWidget()
        self.tabs.addTab(self.variables_tab, "Variables")
        

        self.setCentralWidget(self.tabs)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
