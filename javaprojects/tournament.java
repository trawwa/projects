package javaprojects;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class tournament {
    public static void main(String[] args) {
        List<Player> players = new ArrayList<>();
        Game play;
        makeName();
    }

    private static void makeName() {
        System.out.println("Введите имя игрока: ");
        try (Scanner scanner = new Scanner(System.in)) {
            String name = scanner.nextLine();
        }
    }
}

class Game {
    //pass
    private Player player;

    public Game(){
        player = new Player();
    }


    public Player play() {

        player.makeName();
        return player;
    }
}

class Player {
    private int id;
    private String name;
    private int strengh;

    public Player() {
        this.id = id;
        this.name = name;
        this.strengh = strengh;
    }

    public void makeName() {
        System.out.println("Введите имя игрока: ");
        try (Scanner scanner = new Scanner(System.in)) {
            name = scanner.nextLine();
        }
    }

    public void makeId() {
        System.out.println("Введите ID игрока: ");
        try (Scanner scanner = new Scanner(System.in)) {
            id = scanner.nextInt();
        }
    }

    public void makeStrengh() {
        System.out.println("Введите значение силы игрока: ");
        try (Scanner scanner = new Scanner(System.in)) {
            strengh = scanner.nextInt();
        }
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getStrengh() {
        return strengh;
    }

    public void setStrengh(int strengh) {
        this.strengh = strengh;
    }
}
