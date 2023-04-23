import java.awt.*;
import java.awt.event.*;
import java.sql.SQLException;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.swing.*;
import java.awt.Color;

public class Home{
    private JFrame mainFrame;
    private JLabel headerLabel;
    private JLabel statusLabel;
    ptivate JPanel controlPanel;

    public Home(){
        prepareGUI();
    }

    public static void main(String[] args){
        Home swingControlDemo = new Home();
        swingControlDemo.showButtonDemo();
    }

    private void prepareGUI(){
        mainFrame = new JFrame("Supply Chain Management Systm");
        mainFrame.setBounds(100,100,700,400);
        mainFrame.setLayout(new GridLayout(3,1));
        mainFrame.getContenPane().setBackground(Color.white);
        mainFrame.addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent windowEvent){
                System.exit(0);
            }
        });
        headerLabel = new JLabel("", JLabel.CENTER);
        statusLabel = new JLabel("", JLabel.CENTER);
        statusLabel.setSize(350,300);
        controlPanel = new JPanel();
        controlPanel.setLayout(new GridLayout(1,5));
        mainFrame.add(headerLabel);
        mainFrame.add(controlPanel);
        mainFrame.add(statusLabel);
        mainFrame.setVisible(true);
    }

    public void showButtonDemo(){
        headerLabel.setText("Supply Chain Management System");
        this.headerLabel.setFont(new Font(null, Font.BOLD, 27));
        headerLabel.setForeground(Color.black);
        JButton fkButton = new JButton("Product Details");
        JButton abButton = new JButton("About");
        JButton afButton = new JButton("Product");
        JButton ufButton = new JButton("Supplier Account");
        JButton dlButton = new JButton("Puchase Product");

        fkButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                ItemInfo ii = new ItemInfo();
                ii.showButtonDemo();
            }
        });

        afButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                Home ef = new Home();
                ef.showButtonDemo();
            }
        });

        ufButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                Home uf = new Home(); 
            }
        });

        dlButton.addActionListener(new ActionListener(){
            public void actionPerformed(ActionEvent e){
                Home dl = new Home();
                dl.showButtonDemo();
            }
        });

        controlPanel.add(ufButton);
        controlPanel.add(afButton);
        controlPanel.add(abButton);
        controlPanel.add(fkButton);
        controlPanel.add(dlButton);
        mainFrame.setVisible(true);
        mainFrame.setLocationRelativeTo(null);
    }
}