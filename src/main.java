import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.AnnotationConfiguration;

import javax.swing.*;

public class main {
    static SessionFactory sf;
    static Session s;


    public static void main(String[] args) {
        sf = new AnnotationConfiguration().configure().buildSessionFactory();
        s = sf.openSession();

        JFrame frame = new JFrame("QuestionWindow");
        frame.setContentPane(new QuestionWindow(s).panel1);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);

    }
}