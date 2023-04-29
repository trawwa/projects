import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.loggin.Level;
import java.util.loggin.Logger;

public class Supplier{
    private JFrame mainFrame;
    private JLabel headerLabel;
    private JLabel statusLabel;
    private JPanel controlPanel;
    private JLabel id,name,email,password;
    private static int count = 0;
    GridLayout experimentLayout = new GridLayout(2,2);
    ResultSet rs;

    Supplier(){
        prepareGUI();
    }

    public static void main(String[] args){
        Supplier swingControlDemo = new Supplier();
        swingControlDemo.showButtonDemo();
    }

    private void prepareGUI(){
        mainFrame = new JFrame("Create Supplier Account");
        mainFrame.setSize(700,400);
        mainFrame.setLayout(new GridLayout(3,1));
        mainFrame.getContentPane().setBackground(Color.green);
        mainFrame.addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent windowEvent){
                mainFrame.setVisible(false);
            }
        });
        headerLabel = new JLabel("", JLabel.CENTER);
        statusLabel = new JLabel("", JLabel.CENTER);

        statusLabel.setSize(350,400);

        controlPanel = new JPanel();
        controlPanel.setLayout(350,400);

        mainFrame.add(headerLabel);
        mainFrame.add(controlPanel);
        mainFrame.add(statusLabel);
        mainFrame.setVisible(true);
    }

    public void showButtonDemo(){

        headerLabel.setText("Supply Chain Management System");
        headerLabel.setFont(new Font(null, Font.BOLD, 27));
        headerLabel.setForeground(Color.black);

        name = new JLabel("Enter Supplier Name")
    }
}