import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;

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
        controlPanel.setLayout(new FlowLayout());

        mainFrame.add(headerLabel);
        mainFrame.add(controlPanel);
        mainFrame.add(statusLabel);
        mainFrame.setVisible(true);
    }

    public void showButtonDemo(){

        headerLabel.setText("Supply Chain Management System");
        headerLabel.setFont(new Font(null, Font.BOLD, 27));
        headerLabel.setForeground(Color.black);

        name = new JLabel("Enter Supplier Name");
        JTextField tf2 = new JTextField();
        tf2.setSize(100,30);

        email = new JLabel("Enter Mail Id");
        JTextField tf3 = new JTextField();
        tf3.setSize(100,30);

        password = new JLabel("Enter Password");
        JTextField tf4 = new JTextField();
        tf4.setSize(100,30);

        JButton okButton = new JButton("Create");
        okButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                PreparedStatement pst;
                DBConnection con = new DBConnection();
                try{
                    pst = con.mkDataBase().prepareStatement("UPDATE supplychain SET f_quantity=?, f_prize=? where f_name=?");
                    pst.setString(3, tf2.getText());
                    pst.setDouble(2, Double.parseDouble(tf3.getText()));
                    pst.setInt(1, Integer.parseInt(tf4.getText()));
                    pst.execute();

                    JOptionPane.showMessageDialog(null, "Suplier Account Created!" + tf2.getText());
                    mainFrame.setVisible(false);

                }catch(Exception ex){
                    System.out.println(ex);
                    JOptionPane.showMessageDialog(null, "Error");
                }finally{

                }
            }
        });

        JPanel jp = new JPanel();
        jp.add(name);
        jp.add(tf2);
        jp.add(email);
        jp.add(tf3);
        jp.add(password);
        jp.add(tf4);

        jp.setSize(200,200);
        jp.setLayout(experimentLayout);
        jp.add(okButton);
        mainFrame.setVisible(true);
        mainFrame.setLocationRelativeTo(null);
    }
}