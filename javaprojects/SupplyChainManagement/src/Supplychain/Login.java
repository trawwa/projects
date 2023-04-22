import java.awt.*;
import javax.swing.*;
import javax.swing.colorchooser.AbstractColorChooserPanel;
import java.awt.event.*;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Login extends JFrame {
    JLabel idLabel;
    JLabel passLabel;
    JLabel background;
    JLabel headerLabel;
    JLabel devInfo;
    JTextField id;
    JPasswordField pass;
    JButton sumbit;

    public Loin(){
        setTitle("Supply Chain Management System");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
    }
}