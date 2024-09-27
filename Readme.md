### Problem Statement: Design a Parking Lot System

#### Overview:
You are tasked with designing a parking lot system capable of handling multiple floors and different types of vehicles. The system should be able to accommodate both two-wheeler and four-wheeler vehicles, provide functionality for parking and removing vehicles, and support vehicle lookup by registration number or ticket ID.

#### Requirements:

1. **Parking Lot Structure**:
   - The parking lot has multiple floors. Each floor is divided into rows and columns of parking spots.
   - Parking spots can be designated specifically for two-wheelers (type = 2) or four-wheelers (type = 4).
   - Some spots may be inactive (marked with 0) and should not be available for parking any vehicle.

2. **Functional Requirements**:
   - **Park Vehicles**:
     - Vehicles can be parked using different strategies:
       - **Strategy 0**: Park the vehicle in the first available spot starting from the lowest floor and spot index.
       - **Strategy 1**: Park the vehicle on the floor with the most available spots suitable for that vehicle type. If multiple floors qualify, select the lowest indexed floor.
     - The system should return a unique spot ID in the format "floor-row-column" (e.g., "2-0-15").
   - **Remove Vehicles**:
     - Vehicles can be removed from their parking spot using the spot ID.
     - The system should confirm whether the removal was successful.
   - **Search for Vehicles**:
     - The system should be able to locate a vehicle based on its registration number or the ticket ID provided at the time of parking.
   - **Count Available Spots**:
     - Retrieve the number of free spots available for a specific vehicle type on a given floor.

3. **Logging**:
   - Implement a helper class for logging system actions and messages.

#### Constraints:
- Vehicle types are limited to two-wheeler (2) and four-wheeler (4).
- The parking lot can have between 1 to 5 floors.
- Each floor can have up to 10,000 rows and 10,000 columns, but the total number of spots per floor cannot exceed 10,000.

### Example Scenario:

Consider a parking lot with a single floor structured as follows:

- Floor 0 Layout:
  ```
  [
    [4, 4, 2, 2],
    [2, 4, 2, 0],
    [0, 2, 2, 2],
    [4, 4, 4, 0]
  ]
  ```
- This setup indicates:
  - 7 active spots for two-wheelers and 6 active spots for four-wheelers.
  - Certain spots are inactive and not available for parking (denoted by 0).

#### Actions and Expected Outcomes:

1. **Parking a Two-Wheeler**:
   - Command: `park(2, "BH234", "TKT4534", 0)`
   - Expected Outcome: The system parks the two-wheeler in the first available two-wheeler spot and returns the spot ID `"0-0-2"`.

2. **Searching for a Vehicle**:
   - Command: `search("BH234")` or `search("TKT4534")`
   - Expected Outcome: Returns `"0-0-2"`, indicating the parking spot where the vehicle is located.

3. **Counting Free Spots**:
   - Before Parking: `getFreeSpotsCount(0, 2)` returns `7`.
   - After Parking: `getFreeSpotsCount(0, 2)` returns `6` (one two-wheeler spot is now occupied).

4. **Removing a Parked Vehicle**:
   - Command: `removeVehicle("0-0-2")`
   - Expected Outcome: Returns `True`, indicating successful removal. Subsequent `getFreeSpotsCount(0, 2)` returns `7` again.

This example demonstrates basic operations within the parking lot system, including parking strategies, vehicle removal, and search functionalities tailored for a multi-floor parking structure.

### Problem Statement: Design a Webpage Visits Counter

#### Objective:
Develop a system to track and report the number of visits to individual webpages on a website. The website contains a fixed number of webpages, and it is essential to provide real-time updates on the visit counts. The system must be robust, handling potentially high frequencies of page visit updates and inquiries.

#### Requirements:

1. **System Initialization**:
   - The system should be initialized with the total number of webpages (`totalPages`), which are sequentially numbered from 0 to `n-1`.
   - A helper utility (`helper`) should be provided for logging purposes, aiding in debugging and monitoring system activity.

2. **Functional Requirements**:
   - **Increment Visit Count**:
     - Implement a method `incrementVisitCount(pageIndex)` to increment the visit count for a specific webpage identified by its index (`pageIndex`).
   - **Retrieve Visit Count**:
     - Implement a method `getVisitCount(pageIndex)` to retrieve the current visit count for a specific webpage.

3. **Constraints**:
   - The website consists of at most 1000 webpages.
   - The system should handle a high volume of visits efficiently.
   - The operations for incrementing and retrieving page visit counts must be efficient and capable of handling frequent concurrent requests.

4. **Behavioral Constraints**:
   - The system should not allow concurrent operations for incrementing and retrieving the visit count of the same webpage to maintain data integrity and consistency.
   - Proper error handling should be implemented to manage out-of-range webpage indices or other operational anomalies.

#### Example Workflow:
1. **System Initialization**:
   - Initialize the system with 2 webpages and set up the logging helper.
   - `init(totalPages=2, helper=helper)`

2. **Tracking Page Visits**:
   - Record visits to the webpages:
     - `incrementVisitCount(pageIndex=0)`
     - `incrementVisitCount(pageIndex=1)`
     - `incrementVisitCount(pageIndex=1)`
     - `incrementVisitCount(pageIndex=1)`
     - `incrementVisitCount(pageIndex=0)`

3. **Retrieving Visit Counts**:
   - Retrieve and report the number of visits to each page:
     - `getVisitCount(pageIndex=0)` should return 2 (indicating that the first page was visited twice).
     - `getVisitCount(pageIndex=1)` should return 3 (indicating that the second page was visited three times).

### Use Case:
This system is particularly useful for analytics purposes, helping website administrators understand page popularity, optimize content, and potentially identify bottlenecks or issues based on traffic patterns.

