# Running example

Every example in the templates describes the same fictional equipment rental
business, so that examples agree with each other. Its corpus has documents of
every [concept type](profile.md#concept-types). This page fixes the names
and facts they use. It is illustrative: the [profile](profile.md) and type
contracts remain authoritative, and none of these facts belong in a real
corpus.

A business rents construction equipment from several depots to contractors.
The **rental system** lets customers find and reserve equipment and lets depot
staff hand it over, take it back, and charge for it. **Fleet maintenance** is
a subsystem with its own user class, technicians, who record inspections and
repairs of equipment, and its own external interface to equipment telematics.
Like every user class and external interface, both live at the system level,
and each links Fleet maintenance.

## Names

| Type | Names |
| --- | --- |
| System | Rental system |
| Mission | Rental business mission |
| Vision | Rental business vision |
| Principle | Safe equipment over availability; Contractors' time over depot convenience, in the Rental business principles |
| Job to Be Done | Get equipment on site when the work needs it |
| Business Requirements | Rental system business requirements |
| Subsystem | Fleet maintenance |
| Stakeholder | Equipment insurer |
| User Class | Contractor customer; Depot staff; Technician (Fleet maintenance) |
| External Interface | Payment service; Equipment telematics (Fleet maintenance) |
| Feature | Equipment search; Equipment reservations; Late returns; Site delivery |
| Feature Component | Reservation calendar and Cancellation, within Equipment reservations |
| Use Case | Search for equipment; Reserve equipment; Cancel a reservation; Hand over equipment |
| Requirement | Reservations of unavailable equipment are rejected; Underage rentals are rejected; Reservation notices are sent; Deposits are taken only through the payment service (design constraint); Card payments meet PCI DSS; Reservation pages meet WCAG 2.2 level AA; Handovers can be recorded one-handed; Open reservations are migrated from the previous system |
| Business Rule | Minimum renter age; Overdue inspection withdrawal; Hold period expiry; Customer data retention; High-risk customer; Late return fee |
| Quality Characteristic | Response time; Availability; Confidentiality |
| Quality Requirement | Search responds within limit at peak load; Search withstands a depot outage; Reservations are available; Payment details stay private |
| Measure | Search response time, under Response time; Reservation availability, under Availability |
| Named condition | Peak load, in the rental system's operating environment |
| Business objective | Objective 1; Objective 2 |
| Glossary term | deposit; depot; high-risk customer; hold period; late return; plus entries whose **Defined by** line links the entity and value types below |
| Entity Type | Customer; Equipment item; Rental; Reservation |
| Value Type | Email address; Equipment condition; Money; Operating hours; Rental period |

## Facts

### Direction

- The **rental business** is the business that the rental system serves. Its
  mission is that it keeps contractors working by getting them the equipment
  their work needs, where and when the work needs it.
- Its vision is that contractors have the equipment their work needs on site
  when the work needs it, and never lose a working day to finding, collecting,
  or returning equipment. Business objective 1 is a step toward it.
- Its principles, in order of precedence, are *Safe equipment over
  availability*: it rents only equipment it knows to be safe, even when a
  contractor goes without, from which the Overdue inspection withdrawal rule
  follows; and *Contractors' time over depot convenience*: when a choice saves
  contractors time at the cost of more work for depot staff, it chooses
  contractors' time, which is why customers reserve equipment online at any
  hour.

### Jobs

- The job *Get equipment on site when the work needs it* is performed by
  contractors who run work on a construction site, including site foremen who
  never use the rental system. It arises when work is scheduled on a site for
  a known period and needs equipment the contractor does not own. They seek
  serviceable equipment on site when the crew starts and gone when the work
  ends, with confidence that the start will not slip. Today they call depots,
  borrow from other contractors, buy equipment, or reschedule the work.
- Equipment search, Equipment reservations, and Site delivery serve it, and
  the Problem or opportunity of the business requirements links it.

### Business

- Business objective 1 is that contractor customers reserve equipment without
  calling a depot. Its success indicator is that at least 60% of reservations
  are made online within 12 months of launch.
- Business objective 2 is that fewer rentals are returned late. Its success
  indicator has no agreed target yet, which is an open question.
- The equipment insurer does not use the system; it has an interest in
  equipment with an overdue inspection being withdrawn from rental.

### Terms and data

- A **high-risk customer** is a customer whom the business treats as likely to
  return equipment late; the High-risk customer rule decides who is one.
- A **depot** is a site from which equipment is rented and to which it is
  returned. A **deposit** is an amount authorized against a customer's payment
  card when a reservation is confirmed. A **late return** is the return of
  rented equipment after the last day of its rental period.
- A **reservation** is a customer's commitment to rent specified equipment
  from a depot for one rental period. Each reservation is made by exactly one
  customer, and a customer makes zero or more reservations. A reservation has
  a reservation number of 8 characters that customers quote to depots, a
  confirmation time, and a cancellation time. A reservation's cancellation
  time is not earlier than its confirmation time. A reservation is retained
  after it ends.
- A **rental** is a period during which a customer has the use of equipment,
  beginning when the customer collects it and ending when it is returned.
- A **customer** is a person or company registered to rent equipment. A
  customer remains the same customer when their email address changes. The
  rental system keeps each customer's email address and, for a person, date of
  birth, which is personal data kept to apply the minimum renter age. Payment
  card details are held by the payment service, not the rental system.
- An **equipment item** is identified by its manufacturer serial number, 12
  characters as the manufacturer assigns it. The rental system keeps each
  item's daily rate, replacement value, condition, and operating hours.
- A **rental period** is a span of calendar days during which a customer has
  the use of rented equipment. Its first and last days are inclusive, so a
  one-day rental has the same first and last day, and its last day is not
  earlier than its first. Reservations and rentals both have one.
- **Money** is an amount in a currency: an amount, a decimal to the precision
  of the currency's minor unit, and a currency, an ISO 4217 currency code.
  Amounts are added only in the same currency. Equipment items and rentals
  both hold money.
- An **email address** is an address as defined by RFC 5322. Customers
  have one, and the payment service receives one for each receipt.
- **Equipment condition** is one of *Serviceable*, fit to rent; *Needs
  repair*, not fit to rent until repaired; or *Withdrawn*, removed from rental
  until a technician returns it to service. It is kept for each equipment
  item and reported by equipment telematics.
- **Operating hours** are the whole hours an equipment item's engine has run,
  never negative. They are kept for each equipment item and reported by
  equipment telematics.
- **Fuel level** is a whole-number percentage from 0 to 100 that equipment
  telematics reports. No entity type keeps it and no other interface carries
  it, so it is defined in the telematics interface rather than as a value type.

### Reservations and notices

- A reservation passes through these states: *Held* when the customer
  reserves equipment; *Confirmed* when the deposit is authorized; *Expired*
  when the hold period elapses before the deposit is authorized; *Cancelled*
  when the customer cancels a confirmed reservation; and *Fulfilled* when
  depot staff hand over the equipment. No other transition is permitted.
- The **hold period** is the 30 minutes during which a held reservation keeps
  equipment for the customer. A held reservation must be released when its
  hold period elapses before the deposit is authorized.
- When a reservation is confirmed, expires, or is cancelled, the rental
  system sends the customer a notice within 5 minutes of that change; no other
  reservation notice is sent. The deadline applies to each notice, so it is a
  Requirement.

### Rules

- Equipment may be rented to a customer only if the customer is at least 18
  years old. The rule comes from the business's rental policy, which follows
  national law.
- Equipment whose inspection is overdue must be withdrawn from rental.
- A customer is a high-risk customer if the customer has made three or more
  late returns in the past 12 months.
- The late return fee for a rental is 1.5 times the daily rate for each late
  day, up to the replacement value of the equipment.
- A customer's personal data must be anonymized 6 years after the customer's
  last rental ends, as data protection law requires.

### Features and interfaces

- Equipment search lets contractor customers find available equipment by
  type, depot, and rental period. Site delivery covers only depots that offer
  delivery, and a delivery is arranged for a confirmed reservation. Each
  Equipment search result leads to Reserve equipment.
- The reservation calendar shows, for chosen equipment and a depot, which days
  are available.
- The payment service authorizes deposits, charges fees, and refunds
  deposits, and it sends receipts to the customer's email address. Deposits
  are taken only through the payment service.
- Card payments meet PCI DSS, reservation pages meet WCAG 2.2 level AA, and
  open reservations are migrated from the previous system before launch.
- Depot staff hold equipment while recording a handover, so a handover can be
  recorded one-handed.
- Equipment telematics reports each equipment item's condition, operating
  hours, and fuel level every 15 minutes.

### Quality

- **Peak load** is 2,000 concurrent customers, 80% of them searching. It is a
  named condition in the rental system's operating environment.
- **Search response time** is the 95th percentile of the time from a customer
  submitting a search to the results being shown, over each hour. At peak
  load it is at most 2 seconds. While one depot's network connection is lost,
  search response time for all other depots stays no more than 10% above its
  level in the hour before the loss.
- **Availability** is the proportion of time during which contractor
  customers can reserve equipment. Reservations are available at least 99.5%
  of each calendar month, excluding maintenance announced 48 hours ahead.
- No customer's payment details are revealed to another customer.
