package org.openapis.course;

import org.springframework.web.bind.annotation.*;
import org.openapis.course.model.Error;
import org.openapis.course.model.Pet;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;

import javax.annotation.PostConstruct;
import java.util.HashMap;
import java.util.Map;
import java.util.logging.Logger;

@SpringBootApplication
@RestController
public class CodeFirstApplication {

	private static final Logger logger = Logger.getLogger(CodeFirstApplication.class.getName());

	private static final Integer ALLIGATOR_ID = 1;
	private static final String ALLIGATOR_NAME = "Barnaby";
	private static final String ALLIGATOR_TAG = "Vicious";

	private static final Integer AARDVARK_ID = 2;
	private static final String AARDVARK_NAME = "Colin";
	private static final String AARDVARK_TAG = "Accountant";

	private Map<Integer, Pet> allPetsMap;
	private Integer lastPetId = AARDVARK_ID;

	public static void main(String[] args) {
		SpringApplication.run(CodeFirstApplication.class, args);
	}

	@PostConstruct
	public void init() {
		logger.info("Initialising Pet Map for demo");

		allPetsMap = new HashMap<>();

		// Add pets to Map
		Pet alligator = new Pet();
		alligator.setId(ALLIGATOR_ID);
		alligator.setName(ALLIGATOR_NAME);
		alligator.setTag(ALLIGATOR_TAG);
		allPetsMap.put(ALLIGATOR_ID, alligator);

		Pet aardvark = new Pet();
		aardvark.setId(AARDVARK_ID);
		aardvark.setName(AARDVARK_NAME);
		aardvark.setTag(AARDVARK_TAG);
		allPetsMap.put(AARDVARK_ID, aardvark);
	}

	@Operation(summary = "Get all pets", description = "Retrieve a list of all pets", operationId = "getPets")
	@GetMapping(path = "/pets", produces = { MediaType.APPLICATION_JSON_VALUE })
	@ResponseBody
	public Pet[] getPets() {
		return allPetsMap.values().toArray(new Pet[0]);
	}

	@Operation(summary = "Create a pet", description = "Create a new pet in the system", operationId = "createPet", responses = {
			@ApiResponse(description = "Pet created", responseCode = "201"),
			@ApiResponse(responseCode = "default", content = @Content(schema = @Schema(implementation = Error.class)))
	})
	@PostMapping(path = "/pets", consumes = { MediaType.APPLICATION_JSON_VALUE }, produces = {
			MediaType.APPLICATION_JSON_VALUE })
	public ResponseEntity<?> createPet(@RequestBody Pet pet) {
		if (pet.getName() == null) {
			Error errorResponse = new Error(2000, "Required property not defined: name");
			return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
		}

		Pet newPet = new Pet();
		lastPetId++;
		newPet.setId(lastPetId);
		newPet.setName(pet.getName());
		if (pet.getTag() != null) {
			newPet.setTag(pet.getTag());
		}
		allPetsMap.put(lastPetId, newPet);
		return ResponseEntity.status(HttpStatus.CREATED).build();
	}

	@Operation(summary = "Get pet by ID", description = "Retrieve a pet by its ID", operationId = "getPetById", responses = {
			@ApiResponse(description = "Pet found", responseCode = "200", content = @Content(schema = @Schema(implementation = Pet.class))),
			@ApiResponse(responseCode = "default", content = @Content(schema = @Schema(implementation = Error.class)))
	})
	@GetMapping(path = "/pets/{petId}", produces = { MediaType.APPLICATION_JSON_VALUE })
	@ResponseBody
	public ResponseEntity<?> getPetById(@PathVariable Integer petId) {
		Pet pet = allPetsMap.get(petId);
		if (pet == null) {
			Error errorResponse = new Error(1000, "Unknown Pet identifier");
			return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(errorResponse);
		}
		return ResponseEntity.ok().body(pet);
	}
}
