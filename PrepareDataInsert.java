import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class PrepareDataInsert {
	
	public static void main(String[] args) {
    
		try {
			Scanner in = new Scanner(new File("symptoms.csv"));
			
			in.useDelimiter(",");
			
			// Skip the first three
			in.next();
			in.next();
			in.nextLine();
			
			String insert = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "INSERT DATA {\r\n";
			
			while (in.hasNext()) {
				String disease = in.next();
				disease = disease.replaceAll(" ", "_");
				disease = disease.replaceAll("\\.", "\\\\.");
				disease = disease.replaceAll("'", "\\\\'");
				String symptom = in.next();
				symptom = symptom.replaceAll(" ", "_");
				symptom = symptom.replaceAll("\\.", "\\\\.");
				symptom = symptom.replaceAll("'", "\\\\'");
				
				insert += "\tmed:" + disease + " rdf:type med:Disease .\r\n";
				insert += "\tmed:" + symptom + " rdf:type med:Symptom .\r\n";
				insert += "\tmed:" + disease + " med:hasIndication med:" + symptom + " .\r\n";
				in.nextLine(); // Skip the last column
			}
			
			in = new Scanner(new File("treatment.csv"));
			
			in.useDelimiter(",");
			
			// Skip the first three
			in.next();
			in.next();
			in.nextLine();
			
			while (in.hasNext()) {
				String disease = in.next();
				disease = disease.replaceAll(" ", "_");
				disease = disease.replaceAll("\\.", "\\\\.");
				disease = disease.replaceAll("'", "\\\\'");
				String treatment = in.next();
				treatment = treatment.replaceAll(" ", "_");
				treatment = treatment.replaceAll("\\.", "\\\\.");
				treatment = treatment.replaceAll("'", "\\\\'");
				
				insert += "\tmed:" + disease + " rdf:type med:Disease .\r\n";
				insert += "\tmed:" + treatment + " rdf:type med:Treatment .\r\n";
				insert += "\tmed:" + disease + " med:hasTreatment med:" + treatment + " .\r\n";
				in.nextLine(); // Skip the last column
			}
			
			insert += "}";
			
			File updateFile = new File("update.txt");
			FileWriter updateFileWriter = new FileWriter(updateFile);
			updateFileWriter.write(insert);
			updateFileWriter.close();
			
		} catch (FileNotFoundException fnfe) {} catch (IOException ioe) {}
	}
}
