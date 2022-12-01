import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

import org.apache.jena.query.QueryExecution;
import org.apache.jena.query.QueryExecutionFactory;
import org.apache.jena.query.ResultSet;
import org.apache.jena.query.ResultSetFormatter;
import org.apache.jena.rdf.model.InfModel;
import org.apache.jena.rdf.model.Model;
import org.apache.jena.rdfconnection.RDFConnection;
import org.apache.jena.rdfconnection.RDFConnectionFactory;
import org.apache.jena.update.UpdateExecution;
import org.apache.jena.update.UpdateExecutionFactory;
import org.apache.jena.update.UpdateFactory;
import org.apache.jena.update.UpdateRequest;


public class MedicalConditions {

	static String serviceEndpoint = "http://localhost:3030/Medical/query";
	static String searchCriteria;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		if (args.length < 1) System.exit(1);
		
		String option = args[0];
		
		switch (option) {
		case "update":
			updateDatabase();
			break;
		case "disease":
			findDisease();
			break;
		case "symptom":
			findSymptom();
			break;
		case "treatment":
			findTreatment();
			break;
		}
	}
	
	private static void updateDatabase() {
		File updateFile = new File("update.txt");
		String update = "";
		System.out.println("...");
		try {
			Scanner input = new Scanner(new FileReader(updateFile));
			while (input.hasNextLine()) {
				update += input.nextLine();
			}
		} catch (IOException e) {}
		
		//update = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX med: <http://org.semweb/ser531project/medical#> INSERT DATA { med:Disease_4 rdf:type med:Disease . med:Disease_4 med:hasIndication med:Symptom_A . med:Disease_4 med:hasIndication med:Symptom_C . med:Disease_4 med:hasIndication med:Symptom_D . med:Disease_4 med:treatedBy med:Treatment_V . }";
		
		System.out.println(update);
		RDFConnection conn = RDFConnectionFactory.connect("http://localhost:3030/Medical/update");
		UpdateRequest u = UpdateFactory.create(update);
		
		conn.update(update);
	}
	
	private static void findDisease() {
		File criteriaFile = new File("criteria.txt");
		try {
			Scanner input = new Scanner(new FileReader(criteriaFile));
			searchCriteria = input.nextLine();
		} catch (IOException e) {}
		if (searchCriteria.equals("Enter keywords here...")) {		
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?subject\r\n"
					+ "WHERE {\r\n"
					+ "  ?subject rdf:type med:Disease\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Diseases</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?object\r\n"
					+ "WHERE {\r\n"
					+ "  med:" + searchCriteria + " med:hasIndication ?object\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Symptoms</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.write("<br>");
				
				query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
						+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
						+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
						+ "SELECT ?object\r\n"
						+ "WHERE {\r\n"
						+ "  med:" + searchCriteria + " med:treatedBy ?object\r\n"
						+ "}";
				
				q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
				results = q.execSelect();
				
				resultFW.write("<strong>Treatments</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	private static void findSymptom() {
		File criteriaFile = new File("criteria.txt");
		try {
			Scanner input = new Scanner(new FileReader(criteriaFile));
			searchCriteria = input.nextLine();
		} catch (IOException e) {}
		if (searchCriteria.equals("Enter keywords here...")) {		
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?subject\r\n"
					+ "WHERE {\r\n"
					+ "  ?subject rdf:type med:Symptom\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Symptoms</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?subject\r\n"
					+ "WHERE {\r\n"
					+ "  ?subject  med:hasIndication med:" + searchCriteria + "\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Diseases</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
	
	private static void findTreatment() {
		File criteriaFile = new File("criteria.txt");
		try {
			Scanner input = new Scanner(new FileReader(criteriaFile));
			searchCriteria = input.nextLine();
		} catch (IOException e) {}
		if (searchCriteria.equals("Enter keywords here...")) {		
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?subject\r\n"
					+ "WHERE {\r\n"
					+ "  ?subject rdf:type med:Treatment\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Treatments</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			String query = "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\r\n"
					+ "PREFIX owl: <http://www.w3.org/2002/07/owl#>\r\n"
					+ "PREFIX med: <http://org.semweb/ser531project/medical#>\r\n"
					+ "SELECT ?subject\r\n"
					+ "WHERE {\r\n"
					+ "  ?subject  med:treatedBy med:" + searchCriteria + "\r\n"
					+ "}";
			
			QueryExecution q = QueryExecutionFactory.sparqlService(serviceEndpoint, query);
			ResultSet results = q.execSelect();
			
			File resultFile = new File("result.txt");
			FileWriter resultFW;
			try {
				resultFW = new FileWriter(resultFile);
				resultFW.write("<strong>Diseases</strong><br><br>");
				while (results.hasNext()) {
					String result = results.nextSolution().toString();
					result = result.split("#")[1].split(">")[0];
					resultFW.write(result + "<br>");
				}
				resultFW.close();
				
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}
