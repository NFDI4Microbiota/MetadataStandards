## Built environment microbiome biological/environmental metadata

##   Minimal biological/environmental metadata for Built environmental microbiome

| Category | MIXS ID | Metadata field | Brief description | Definition | Example of Annotation | Source |
| --- | --- | --- | --- | --- | --- | --- |
| **Sample metadata** | [\[MIXS:0000103\]](https://w3id.org/mixs/0000103) | organism_count | organism count | Total cell count of any organism (or group of organisms) per gram, volume or area of sample, should include name of organism followed by count. The method that was used for the enumeration (e.g. qPCR, atp, mpn, etc.) Should also be provided. (example: total prokaryotes; 3.5e7 cells per ml; qpcr) | total bacteria; 2.1 × 10⁶ cells cm⁻²; Real Time PCR [\[NCIT:C51962\]](http://purl.obolibrary.org/obo/NCIT_C51962) |  |
|  | [\[MIXS:0001107\]](https://w3id.org/mixs/0001107) | samp_name | sample name | A local identifier or name that for the material sample used for extracting nucleic acids, and subsequent sequencing. It can refer either to the original material collected or to any derived sub-samples. It can have any format, but we suggest that you make it concise, unique and consistent within your lab, and as informative as possible. INSDC requires every sample name from a single Submitter to be unique. Use of a globally unique identifier for the field source_mat_id is recommended in addition to sample_name | NY_LR_Dust_2023-10-15 |  |
|  | [\[MIXS:0000001\]](https://w3id.org/mixs/0000001) | samp_size | amount or size of sample collected | The total amount or size (volume (ml), mass (g) or area (m2) ) of sample collected | 1 g |  |
|  | [\[MIXS:0000016\]](https://w3id.org/mixs/0000016) | samp_mat_process | sample material processing | A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed | dust collected via sterile nylon-filter vacuum; sieved < 300 µm; stored −80 °C |  |
|  | [\[MIXS:0000026\]](https://w3id.org/mixs/0000026) | source_mat_id | source material identifiers | A unique identifier assigned to a material sample (as defined by http://rs.tdwg.org/dwc/terms/materialSampleID, and as opposed to a particular digital record of a material sample) used for extracting nucleic acids, and subsequent sequencing. The identifier can refer either to the original material collected or to any derived sub-samples. The INSDC qualifiers /specimen_voucher, /bio_material, or /culture_collection may or may not share the same value as the source_mat_id field. For instance, the /specimen_voucher qualifier and source_mat_id may both contain 'UAM:Herps:14' , referring to both the specimen voucher and sampled tissue with the same identifier. However, the /culture_collection qualifier may refer to a value from an initial culture (e.g. ATCC:11775) while source_mat_id would refer to an identifier from some derived culture from which the nucleic acids were extracted (e.g. xatc123 or ark:/2154/R2) | NY_LR_5B_20231015_01 |  |
|  | [\[MIXS:0000325\]](https://w3id.org/mixs/0000325) | pool_dna_extracts | pooling of DNA extracts (if done) | Indicate whether multiple DNA extractions were mixed. If the answer yes, the number of extracts that were pooled should be given | no |  |
|  | [\[MIXS:0000590\]](https://w3id.org/mixs/0000590) | water_temp_regm | water temperature regimen | Information about treatment involving an exposure to water with varying degree of temperature, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens | not applicable |  |
|  | [\[MIXS:0000591\]](https://w3id.org/mixs/0000591) | watering_regm | watering regimen | Information about treatment involving an exposure to watering frequencies, treatment regimen including how many times the treatment was repeated, how long each treatment lasted, and the start and end time of the entire treatment; can include multiple regimens | not applicable |  |
|  | [\[MIXS:0001153\]](https://w3id.org/mixs/0001153) | samp_pooling | sample pooling | Physical combination of several instances of like material, e.g. RNA extracted from samples or dishes of cell cultures into one big aliquot of cells. Please provide a short description of the samples that were pooled | none |  |
| **Site metadata** | [\[MIXS:0000092\]](https://w3id.org/mixs/0000092) | project_name | project name | Name of the project within which the sequencing was organized | Indoor Microbiome NYC-Apartment Study |  |
|  | [\[MIXS:0000097\]](https://w3id.org/mixs/0000097) | carb_dioxide | carbon dioxide | Carbon dioxide (gas) amount or concentration at the time of sampling | 800 ppm |  |
|  | [\[MIXS:0000121\]](https://w3id.org/mixs/0000121) | rel_air_humidity | relative air humidity | Partial vapor and air pressure, density of the vapor and air, or by the actual mass of the vapor and air | 45 % RH |  |
|  | [\[MIXS:0000124\]](https://w3id.org/mixs/0000124) | air_temp | air temperature | Temperature of the air at the time of sampling | 22 °C |  |
|  | [\[MIXS:0000125\]](https://w3id.org/mixs/0000125) | surf_temp | surface temperature | Temperature of the surface at the time of sampling | 20 °C |  |
|  | [\[MIXS:0000128\]](https://w3id.org/mixs/0000128) | surf_moisture | surface moisture | Water held on a surface | 0.15 g H₂O g⁻¹ surface |  |
|  | [\[MIXS:0000140\]](https://w3id.org/mixs/0000140) | amount_light | amount of light | The unit of illuminance and luminous emittance, measuring luminous flux per unit area | 300 lux |  |
|  | [\[MIXS:0000145\]](https://w3id.org/mixs/0000145) | built_struc_age | built structure age | The age of the built structure since construction | 12 y |  |
|  | [\[MIXS:0000165\]](https://w3id.org/mixs/0000165) | floor_area | floor area | The area of the floor space within the room | 25 m² |  |
|  | [\[MIXS:0000168\]](https://w3id.org/mixs/0000168) | inside_lux | inside lux light | The recorded value at sampling time (power density) | 250 lux |  |
|  | [\[MIXS:0000192\]](https://w3id.org/mixs/0000192) | room_dim | room dimensions | The length, width and height of sampling room | 5 m × 5 m × 2.5 m |  |
|  | [\[MIXS:0000195\]](https://w3id.org/mixs/0000195) | room_vol | room volume | Volume of sampling room | 62.5 m³ |  |
|  | [\[MIXS:0000197\]](https://w3id.org/mixs/0000197) | temp_out | temperature outside house | The recorded temperature value at sampling time outside | 18 °C |  |
|  | [\[MIXS:0000217\]](https://w3id.org/mixs/0000217) | occup_density_samp | occupant density at sampling | Average number of occupants at time of sampling per square footage | 0.08 persons m⁻² (2 occupants / 25 m²) |  |
|  | [\[MIXS:0000218\]](https://w3id.org/mixs/0000218) | address | address | The street name and building number where the sampling occurred | 123 Main St., Apt 5B, New York, NY 10001 |  |
|  | [\[MIXS:0000224\]](https://w3id.org/mixs/0000224) | window_size | window area/size | The window's length and width | 1.2 m × 1.5 m |  |
|  | [\[MIXS:0000225\]](https://w3id.org/mixs/0000225) | floor_count | floor count | The number of floors in the building, including basements and mechanical penthouse | 6 |  |
|  | [\[MIXS:0000226\]](https://w3id.org/mixs/0000226) | freq_clean | frequency of cleaning | The number of times the sample location is cleaned. Frequency of cleaning might be on a Daily basis, Weekly, Monthly, Quarterly or Annually | weekly |  |
|  | [\[MIXS:0000230\]](https://w3id.org/mixs/0000230) | number_plants | number of houseplants | The number of plant(s) in the sampling space | 2 |  |
|  | [\[MIXS:0000231\]](https://w3id.org/mixs/0000231) | number_pets | number of pets | The number of pets residing in the sampled space | 1 cat |  |
|  | [\[MIXS:0000232\]](https://w3id.org/mixs/0000232) | number_resident | number of residents | The number of individuals currently occupying in the sampling location | 2 |  |
|  | [\[MIXS:0000234\]](https://w3id.org/mixs/0000234) | room_count | room count | The total count of rooms in the built structure including all room types | 3 |  |
|  | [\[MIXS:0000235\]](https://w3id.org/mixs/0000235) | room_moist_dam_hist | room moisture damage or mold history | The history of moisture damage or mold in the past 12 months. Number of events of moisture damage or mold observed | 0 events |  |
|  | [\[MIXS:0000236\]](https://w3id.org/mixs/0000236) | room_occup | room occupancy | Count of room occupancy at time of sampling | 2 |  |
|  | [\[MIXS:0000237\]](https://w3id.org/mixs/0000237) | room_window_count | room window count | Number of windows in the room | 2 |  |
|  | [\[MIXS:0000244\]](https://w3id.org/mixs/0000244) | samp_room_id | sampling room ID or name | Sampling room number. This ID should be consistent with the designations on the building floor plans | LR_apt5B |  |
|  | [\[MIXS:0000756\]](https://w3id.org/mixs/0000756) | ventilation_type | ventilation type | Ventilation system used in the sampled premises | central HVAC \| operable window |  |
|  | [\[MIXS:0000758\]](https://w3id.org/mixs/0000758) | surf_material | surface material | Surface materials at the point of sampling | painted drywall |  |
|  | [\[MIXS:0000761\]](https://w3id.org/mixs/0000761) | build_occup_type | building occupancy type | The primary function for which a building or discrete part of a building is intended to be used | residential dwelling unit |  |
|  | [\[MIXS:0000764\]](https://w3id.org/mixs/0000764) | indoor_surf | indoor surface | Type of indoor surface | wall |  |
|  | [\[MIXS:0000765\]](https://w3id.org/mixs/0000765) | filter_type | filter type | A device which removes solid particulates or airborne molecular contaminants | MERV-13 pleated filter |  |
|  | [\[MIXS:0000766\]](https://w3id.org/mixs/0000766) | heat_cool_type | heating and cooling system type | Methods of conditioning or heating a room or building | forced-air heating & cooling |  |
|  | [\[MIXS:0000768\]](https://w3id.org/mixs/0000768) | building_setting | building setting | A location (geography) where a building is set | urban residential high-rise |  |
|  | [\[MIXS:0000769\]](https://w3id.org/mixs/0000769) | light_type | light type | Application of light to achieve some practical or aesthetic effect. Lighting includes the use of both artificial light sources such as lamps and light fixtures, as well as natural illumination by capturing daylight. Can also include absence of light | LED ceiling light \| natural daylight |  |
|  | [\[MIXS:0000772\]](https://w3id.org/mixs/0000772) | occup_samp | occupancy at sampling | Number of occupants present at time of sample within the given space | 2 |  |
|  | [\[MIXS:0000778\]](https://w3id.org/mixs/0000778) | built_struc_set | built structure setting | The characterization of the location of the built structure as high or low human density | high human density |  |
|  | [\[MIXS:0000803\]](https://w3id.org/mixs/0000803) | floor_cond | floor condition | The physical condition of the floor at the time of sampling; photos or video preferred; use drawings to indicate location of damaged areas | clean; no visible damage |  |
|  | [\[MIXS:0000804\]](https://w3id.org/mixs/0000804) | floor_finish_mat | floor finish material | The floor covering type; the finished surface that is walked on | hardwood |  |
|  | [\[MIXS:0000805\]](https://w3id.org/mixs/0000805) | floor_water_mold | floor signs of water/mold | Signs of the presence of mold or mildew in a room | none |  |
|  | [\[MIXS:0000808\]](https://w3id.org/mixs/0000808) | gender_restroom | gender of restroom | The gender type of the restroom | unisex |  |
|  | [\[MIXS:0000814\]](https://w3id.org/mixs/0000814) | last_clean | last time swept/mopped/vacuumed | The last time the floor was cleaned (swept, mopped, vacuumed) | 2023-10-15T07:00:00Z |  |
|  | [\[MIXS:0000819\]](https://w3id.org/mixs/0000819) | pres_animal_insect | presence of pets, animals, or insects | The type and number of animals or insects present in the sampling space | Blattella germanica [\[NCBI:txid6973\]](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=6973&lvl=3&lin=f&keep=1&srchmode=1&unlock) (German cockroach); 1 |  |
|  | [\[MIXS:0000822\]](https://w3id.org/mixs/0000822) | room_condt | room condition | The condition of the room at the time of sampling | tidy |  |
|  | [\[MIXS:0000825\]](https://w3id.org/mixs/0000825) | room_type | room type | The main purpose or activity of the sampling room. A room is any distinguishable space within a structure | living room |  |
|  | [\[MIXS:0000828\]](https://w3id.org/mixs/0000828) | samp_floor | sampling floor | The floor of the building, where the sampling room is located | 5 |  |
|  | [\[MIXS:0000844\]](https://w3id.org/mixs/0000844) | wall_water_mold | wall signs of water/mold | Signs of the presence of mold or mildew on a wall | none |  |
|  | [\[MIXS:0000854\]](https://w3id.org/mixs/0000854) | window_water_mold | window signs of water/mold | Signs of the presence of mold or mildew on the window | none |  |
|  | [\[MIXS:0000856\]](https://w3id.org/mixs/0000856) | window_type | window type | The type of windows | double-glazed sliding |  |
|  | [\[MIXS:0000093\]](https://w3id.org/mixs/0000093) | elev | elevation | Elevation of the sampling site is its height above a fixed reference point, most commonly the mean sea level. Elevation is mainly used when referring to points on the earth's surface, while altitude is used for points above the surface, such as an aircraft in flight or a spacecraft in orbit | 30 m |  |
|  | [\[MIXS:0000100\]](https://w3id.org/mixs/0000100) | humidity | humidity | Amount of water vapour in the air, at the time of sampling | 48 % RH |  |
|  | [\[MIXS:0001086\]](https://w3id.org/mixs/0001086) | fire | history/fire | Historical and/or physical evidence of fire | none |  |
|  | [\[MIXS:0001121\]](https://w3id.org/mixs/0001121) | adjacent_environment | environment adjacent to site | Description of the environmental system or features that are adjacent to the sampling site. This field accepts terms under ecosystem (http://purl.obolibrary.org/obo/ENVO_01001110) and human construction (http://purl.obolibrary.org/obo/ENVO_00000070). Multiple terms can be separated by pipes | public park [\[ENVO:03500002\]](http://purl.obolibrary.org/obo/ENVO_03500002) |  |

# References

“MIMS: Metagenome/Environmental, Human-Associated; Version 6.0 Package.”
<https://www.ncbi.nlm.nih.gov/biosample/docs/packages/MIMS.me.human-associated.5.0/>.

"GSC MIxS: BuiltEnvironmentMIMS"
<https://genomicsstandardsconsortium.github.io/mixs/0016001/>