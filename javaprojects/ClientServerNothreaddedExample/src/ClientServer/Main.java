package javaprojects.ClientServerNothreaddedExample.src.ClientServer;

import java.io.IOException;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) throws InterruptedException, SQLException, IOException {
        Server serverSocket = new Server(5050, 100000);
        serverSocket.run();
    }
}
