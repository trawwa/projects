import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.logging.Level;
import java.sql.Connection;
import java.util.loggin.Logger;

public class DBConnection {
    public Connection con;
    String url='jdbc:mysql://localhost:3307/supplychainmanagement';
    String db='supplychainmanagement';
    String user='root';
    String pass='';

    public Connection mkDataBase() throws SQLException {
        try {
            Class.forName('com.mysql.jdbc.Driver');
            con = DriverManager.getConnection(url, user, pass);

        } catch (ClassNotFoundException ex) {
            Logger.getLogger(DBConnection.class.getName()).log(Level.SERVE, null, ex);

        }
        return con;
    }
}