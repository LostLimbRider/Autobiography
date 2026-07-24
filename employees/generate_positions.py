#!/usr/bin/env python3
"""
Position Manual Generator for Lost Limb Riders

This script generates position manuals for all organizational roles.
Run this script to create or update all position documentation.

Usage: python3 generate_positions.py
Output: Creates position manual files in the employees/ directory
"""

import os
import sys

# Position data with detailed information
POSITIONS = [
    {
        "number": "01",
        "name": "Chairperson",
        "filename": "01-Chairperson.md",
        "purpose": "Lead board governance and protect mission accountability.",
        "responsibilities": [
            "Set board meeting agendas with Executive Leadership",
            "Facilitate board meetings with clear structure and decisive closure",
            "Ensure all directors receive meeting materials timely",
            "Maintain accurate records through coordination with Secretary",
            "Call emergency meetings when necessary",
            "Oversee standing committee effectiveness",
            "Coordinate annual executive performance review",
            "Enforce Board Code of Conduct and Conflict of Interest Policy"
        ],
        "reporting": "Board of Directors",
        "time": "6-12 hours monthly"
    },
    {
        "number": "02",
        "name": "Vice Chairperson",
        "filename": "02-Vice-Chairperson.md",
        "purpose": "Support governance continuity and serve as Chairperson backup.",
        "responsibilities": [
            "Consult with Chairperson on meeting agendas and governance strategy",
            "Assume all Chairperson duties when Chairperson unavailable",
            "Lead special board initiatives and governance projects",
            "Support recruitment of new directors",
            "Mentor newer directors on governance responsibilities",
            "Serve on at least one standing committee"
        ],
        "reporting": "Board of Directors",
        "time": "4-8 hours monthly"
    },
    {
        "number": "03",
        "name": "Secretary",
        "filename": "03-Secretary.md",
        "purpose": "Maintain official records and governance documentation.",
        "responsibilities": [
            "Take comprehensive minutes at all Board meetings",
            "Document motions, votes, abstentions, and recusals",
            "Maintain official director roster and contact information",
            "Keep bylaws and adopted policies in accessible format",
            "Preserve Board resolutions and formal decisions",
            "Send proper notice of all Board meetings per bylaws",
            "Archive and organize all governance records"
        ],
        "reporting": "Board of Directors",
        "time": "4-8 hours monthly"
    },
    {
        "number": "04",
        "name": "Treasurer",
        "filename": "04-Treasurer.md",
        "purpose": "Provide financial oversight and governance.",
        "responsibilities": [
            "Review monthly financial statements and variance reports",
            "Verify accuracy of income, expense, and fund balance reporting",
            "Chair the Finance Committee",
            "Present budget to Board with narrative explanation",
            "Confirm that approval authorities are followed",
            "Ensure segregation of duties in financial management",
            "Prepare for external audits"
        ],
        "reporting": "Board of Directors",
        "time": "6-10 hours monthly"
    },
    {
        "number": "05",
        "name": "At-Large Director",
        "filename": "05-At-Large-Director.md",
        "purpose": "Provide independent oversight and mission support.",
        "responsibilities": [
            "Attend all Board meetings and actively participate",
            "Serve on at least one standing committee",
            "Champion the organization's mission in networks",
            "Support fundraising goals and make annual contribution",
            "Participate in policy review and recommendations",
            "Represent community perspective in Board discussions"
        ],
        "reporting": "Board of Directors",
        "time": "4-8 hours monthly"
    },
    {
        "number": "06",
        "name": "Founder / CEO",
        "filename": "06-Founder-CEO.md",
        "purpose": "Protect founding vision and public mission.",
        "responsibilities": [
            "Be the primary voice advocating for community",
            "Build and maintain major healthcare partnerships",
            "Serve as primary public spokesperson",
            "Give keynote speeches and represent organization",
            "Provide strategic counsel to Board of Directors",
            "Model organizational values and commitment to mission",
            "Leverage personal lived experience for organizational benefit"
        ],
        "reporting": "Board of Directors",
        "time": "Board-approved; typically significant"
    },
    {
        "number": "07",
        "name": "Executive Director",
        "filename": "07-Executive-Director.md",
        "purpose": "Manage daily operations and implement Board strategy.",
        "responsibilities": [
            "Recruit, hire, and supervise all staff positions",
            "Manage daily operations of all departments",
            "Execute Board-approved annual budget",
            "Monitor spending and financial planning",
            "Ensure all programs operate safely and effectively",
            "Provide executive reports to Board at each meeting",
            "Ensure compliance with nonprofit laws and regulations"
        ],
        "reporting": "Board of Directors",
        "time": "Full-time (40-60 hours weekly)"
    },
    {
        "number": "08",
        "name": "Deputy Executive Director",
        "filename": "08-Deputy-Executive-Director.md",
        "purpose": "Support executive operations and ensure continuity.",
        "responsibilities": [
            "Facilitate communication between departments",
            "Manage inter-department projects and initiatives",
            "Lead special organizational initiatives",
            "Support chapter development and growth",
            "Assume Executive Director duties when ED unavailable",
            "Maintain documentation of critical operations"
        ],
        "reporting": "Executive Director",
        "time": "Part-time to full-time (30-40 hours weekly)"
    },
    {
        "number": "09",
        "name": "Director of Administration",
        "filename": "09-Director-of-Administration.md",
        "purpose": "Lead administrative systems and operations.",
        "responsibilities": [
            "Establish and maintain official organizational records",
            "Develop records retention and destruction procedures",
            "Manage office space, equipment, and supplies",
            "Maintain master organizational calendar",
            "Track required licenses, permits, and registrations",
            "Supervise administrative staff"
        ],
        "reporting": "Executive Director",
        "time": "5-15 hours weekly"
    },
    {
        "number": "10",
        "name": "Administrative Assistant",
        "filename": "10-Administrative-Assistant.md",
        "purpose": "Provide administrative support to leadership.",
        "responsibilities": [
            "Maintain calendars for Executive Director",
            "Schedule meetings and coordinate participants",
            "Manage incoming mail and email routing",
            "Maintain organized filing systems",
            "Support Board and committee meetings",
            "Monitor office supplies and equipment"
        ],
        "reporting": "Director of Administration",
        "time": "3-10 hours weekly"
    },
    {
        "number": "11",
        "name": "Records Compliance Officer",
        "filename": "11-Records-Compliance-Officer.md",
        "purpose": "Protect official records and retention standards.",
        "responsibilities": [
            "Develop and maintain records retention schedule",
            "Control access to sensitive records",
            "Maintain compliance files and documentation",
            "Conduct annual records review and audit",
            "Ensure records management policy compliance",
            "Archive and safely destroy records per policy"
        ],
        "reporting": "Director of Administration",
        "time": "2-6 hours weekly"
    },
    {
        "number": "12",
        "name": "Membership Director",
        "filename": "12-Membership-Director.md",
        "purpose": "Lead member recruitment and retention.",
        "responsibilities": [
            "Develop membership strategy and growth plan",
            "Oversee member onboarding process",
            "Manage membership renewals and retention",
            "Support chapter membership coordination",
            "Communicate with members on benefits",
            "Maintain accurate membership database"
        ],
        "reporting": "Executive Director",
        "time": "5-12 hours weekly"
    },
    {
        "number": "13",
        "name": "Membership Coordinator",
        "filename": "13-Membership-Coordinator.md",
        "purpose": "Maintain member services and database.",
        "responsibilities": [
            "Process membership applications",
            "Send welcome messages and materials",
            "Update membership roster",
            "Send renewal reminders",
            "Answer member questions and support",
            "Maintain data accuracy and confidentiality"
        ],
        "reporting": "Membership Director",
        "time": "3-8 hours weekly"
    },
    {
        "number": "14",
        "name": "Chapter Director",
        "filename": "14-Chapter-Director.md",
        "purpose": "Lead local chapter operations.",
        "responsibilities": [
            "Organize and lead local chapter meetings",
            "Report to national organization",
            "Coordinate chapter volunteers",
            "Engage local partners and community",
            "Ensure safety compliance at chapter events",
            "Build healthy chapter culture",
            "Lead chapter rides and activities"
        ],
        "reporting": "Membership Director",
        "time": "5-15 hours weekly"
    },
    {
        "number": "15",
        "name": "Family Support Director",
        "filename": "15-Family-Support-Director.md",
        "purpose": "Lead participant and family support programs.",
        "responsibilities": [
            "Oversee participant intake and support",
            "Manage peer mentor matching process",
            "Coordinate referral system",
            "Maintain confidentiality standards",
            "Handle crisis escalation and response",
            "Develop support program strategy",
            "Supervise family support staff"
        ],
        "reporting": "Executive Director",
        "time": "5-15 hours weekly"
    },
    {
        "number": "16",
        "name": "Peer Support Coordinator",
        "filename": "16-Peer-Support-Coordinator.md",
        "purpose": "Manage peer mentors and support program.",
        "responsibilities": [
            "Recruit and screen peer mentors",
            "Provide mentor training and development",
            "Match mentors with participants",
            "Supervise mentor relationships",
            "Conduct mentor debriefing sessions",
            "Address mentor concerns or issues",
            "Track support outcomes"
        ],
        "reporting": "Family Support Director",
        "time": "3-10 hours weekly"
    },
    {
        "number": "17",
        "name": "Family Advocate",
        "filename": "17-Family-Advocate.md",
        "purpose": "Support families and caregivers.",
        "responsibilities": [
            "Provide listening support to families",
            "Navigate families through resources",
            "Conduct regular caregiver check-ins",
            "Document referrals and support provided",
            "Build family engagement",
            "Coordinate with support services",
            "Maintain boundaries and confidentiality"
        ],
        "reporting": "Family Support Director",
        "time": "2-8 hours weekly"
    },
    {
        "number": "18",
        "name": "Crisis Resource Coordinator",
        "filename": "18-Crisis-Resource-Coordinator.md",
        "purpose": "Manage crisis escalation and resources.",
        "responsibilities": [
            "Train organization on crisis protocols",
            "Coordinate urgent referrals",
            "Maintain updated resource database",
            "Document crisis incidents",
            "Develop crisis response procedures",
            "Coordinate with emergency services",
            "Provide crisis follow-up support"
        ],
        "reporting": "Family Support Director",
        "time": "On-call schedule as needed"
    },
    {
        "number": "19",
        "name": "Outreach Director",
        "filename": "19-Outreach-Director.md",
        "purpose": "Lead institutional and community partnerships.",
        "responsibilities": [
            "Develop outreach strategy",
            "Build hospital and rehab relationships",
            "Negotiate partnership agreements",
            "Lead organizational presentations",
            "Coordinate community engagement",
            "Oversee outreach staff",
            "Track partnership outcomes"
        ],
        "reporting": "Executive Director",
        "time": "5-12 hours weekly"
    },
    {
        "number": "20",
        "name": "Hospital Liaison",
        "filename": "20-Hospital-Liaison.md",
        "purpose": "Build hospital and rehabilitation relationships.",
        "responsibilities": [
            "Maintain facility contact relationships",
            "Coordinate peer support visits",
            "Follow facility policies and procedures",
            "Communicate referrals with facilities",
            "Represent organization professionally",
            "Report on facility interactions",
            "Address facility concerns"
        ],
        "reporting": "Outreach Director",
        "time": "3-8 hours weekly"
    },
    {
        "number": "21",
        "name": "Community Relations Coordinator",
        "filename": "21-Community-Relations-Coordinator.md",
        "purpose": "Connect with civic and community groups.",
        "responsibilities": [
            "Give presentations to community groups",
            "Participate in resource fairs",
            "Maintain partner database",
            "Follow up with community contacts",
            "Build community awareness",
            "Coordinate community volunteers",
            "Represent organization at events"
        ],
        "reporting": "Outreach Director",
        "time": "3-8 hours weekly"
    },
    {
        "number": "22",
        "name": "Riding Operations Director",
        "filename": "22-Riding-Operations-Director.md",
        "purpose": "Lead safe motorcycle operations.",
        "responsibilities": [
            "Establish ride safety standards",
            "Approve ride routes and dates",
            "Train ride captains",
            "Review ride reports and safety",
            "Address safety concerns",
            "Coordinate with ride captains",
            "Ensure compliance with insurance"
        ],
        "reporting": "Executive Director",
        "time": "5-12 hours weekly during riding season"
    },
    {
        "number": "23",
        "name": "Ride Captain",
        "filename": "23-Ride-Captain.md",
        "purpose": "Lead individual motorcycle rides.",
        "responsibilities": [
            "Brief riders on route and safety",
            "Check rider experience level",
            "Control pace and stops",
            "Manage emergency situations",
            "Communicate with sweep riders",
            "Report on ride completion",
            "Maintain ride documentation"
        ],
        "reporting": "Riding Operations Director",
        "time": "Per ride plus preparation"
    },
    {
        "number": "24",
        "name": "Safety Officer",
        "filename": "24-Safety-Officer.md",
        "purpose": "Monitor ride and event safety.",
        "responsibilities": [
            "Identify hazards and risks",
            "Provide safety briefings",
            "Report incidents and near-misses",
            "Recommend safety improvements",
            "Stop unsafe activity",
            "Maintain safety documentation",
            "Support training and compliance"
        ],
        "reporting": "Riding Operations Director",
        "time": "Per event or ride"
    },
    {
        "number": "25",
        "name": "Road Guard Team",
        "filename": "25-Road-Guard-Team.md",
        "purpose": "Support ride flow at authorized locations.",
        "responsibilities": [
            "Position at assigned road locations",
            "Communicate with ride group",
            "Assist riders with route",
            "Alert to hazards",
            "Follow local traffic laws",
            "Maintain safety discipline",
            "Support ride objectives"
        ],
        "reporting": "Ride Captain",
        "time": "Per ride"
    },
    {
        "number": "26",
        "name": "Events Director",
        "filename": "26-Events-Director.md",
        "purpose": "Lead organizational events.",
        "responsibilities": [
            "Plan annual event calendar",
            "Develop event budgets",
            "Manage logistics and permits",
            "Develop volunteer plans",
            "Coordinate with venues",
            "Evaluate event success",
            "Report on outcomes"
        ],
        "reporting": "Executive Director",
        "time": "5-15 hours weekly during event cycles"
    },
    {
        "number": "27",
        "name": "Event Coordinator",
        "filename": "27-Event-Coordinator.md",
        "purpose": "Execute event logistics.",
        "responsibilities": [
            "Coordinate with venues",
            "Organize supplies and materials",
            "Create and manage schedules",
            "Communicate with vendors",
            "Execute setup and breakdown",
            "Manage event checklists",
            "Support event day operations"
        ],
        "reporting": "Events Director",
        "time": "Per event cycle"
    },
    {
        "number": "28",
        "name": "Volunteer Coordinator",
        "filename": "28-Volunteer-Coordinator.md",
        "purpose": "Recruit, schedule, and support volunteers.",
        "responsibilities": [
            "Recruit volunteer applicants",
            "Conduct volunteer orientation",
            "Create volunteer schedules",
            "Assign volunteer roles",
            "Recognize volunteer contributions",
            "Address volunteer issues",
            "Maintain volunteer database"
        ],
        "reporting": "Events Director or Director of Administration",
        "time": "3-10 hours weekly"
    },
    {
        "number": "29",
        "name": "Fundraising Director",
        "filename": "29-Fundraising-Director.md",
        "purpose": "Lead revenue development.",
        "responsibilities": [
            "Develop fundraising strategy",
            "Cultivate major donors",
            "Coordinate fundraising campaigns",
            "Oversee grant coordination",
            "Manage sponsorship program",
            "Track fundraising outcomes",
            "Report on revenue progress"
        ],
        "reporting": "Executive Director",
        "time": "5-15 hours weekly"
    },
    {
        "number": "30",
        "name": "Grant Writer",
        "filename": "30-Grant-Writer.md",
        "purpose": "Develop grant applications and reports.",
        "responsibilities": [
            "Research grant opportunities",
            "Write grant narratives",
            "Develop grant budgets",
            "Submit grant applications",
            "Track submission deadlines",
            "Prepare grant reports",
            "Maintain grant documentation"
        ],
        "reporting": "Fundraising Director",
        "time": "Project-based"
    },
    {
        "number": "31",
        "name": "Sponsorship Coordinator",
        "filename": "31-Sponsorship-Coordinator.md",
        "purpose": "Manage corporate sponsors.",
        "responsibilities": [
            "Develop sponsorship packages",
            "Reach out to potential sponsors",
            "Negotiate sponsorship agreements",
            "Fulfill sponsor benefits",
            "Track sponsorship renewals",
            "Report on sponsorship value",
            "Maintain sponsor relationships"
        ],
        "reporting": "Fundraising Director",
        "time": "3-10 hours weekly"
    },
    {
        "number": "32",
        "name": "Donor Relations Manager",
        "filename": "32-Donor-Relations-Manager.md",
        "purpose": "Steward donors and major supporters.",
        "responsibilities": [
            "Send donor acknowledgments",
            "Provide donor updates",
            "Recognize donor contributions",
            "Maintain donor records",
            "Conduct donor outreach",
            "Plan donor events",
            "Support donor retention"
        ],
        "reporting": "Fundraising Director",
        "time": "3-8 hours weekly"
    },
    {
        "number": "33",
        "name": "Finance Director",
        "filename": "33-Finance-Director.md",
        "purpose": "Lead financial administration.",
        "responsibilities": [
            "Develop annual budget",
            "Prepare financial reports",
            "Establish internal controls",
            "Coordinate with Treasurer",
            "Manage financial calendar",
            "Support audits",
            "Provide financial analysis"
        ],
        "reporting": "Executive Director with Treasurer oversight",
        "time": "5-12 hours weekly"
    },
    {
        "number": "34",
        "name": "Bookkeeper",
        "filename": "34-Bookkeeper.md",
        "purpose": "Maintain financial records.",
        "responsibilities": [
            "Record financial transactions",
            "Reconcile accounts",
            "Maintain payable records",
            "Maintain receivable records",
            "Document transactions",
            "Prepare monthly reports",
            "Support audit process"
        ],
        "reporting": "Finance Director",
        "time": "3-10 hours weekly"
    },
    {
        "number": "35",
        "name": "Purchasing Officer",
        "filename": "35-Purchasing-Officer.md",
        "purpose": "Manage purchasing controls.",
        "responsibilities": [
            "Process purchase requests",
            "Obtain quotes for purchases",
            "Track receipts",
            "Maintain vendor files",
            "Ensure policy compliance",
            "Track purchase budgets",
            "Report on spending"
        ],
        "reporting": "Finance Director",
        "time": "2-6 hours weekly"
    },
    {
        "number": "36",
        "name": "Communications Director",
        "filename": "36-Communications-Director.md",
        "purpose": "Lead public messaging and brand.",
        "responsibilities": [
            "Develop communications strategy",
            "Establish brand standards",
            "Review media and communications",
            "Tell organizational stories",
            "Coordinate crisis communication",
            "Oversee communications staff",
            "Manage external messaging"
        ],
        "reporting": "Executive Director",
        "time": "5-12 hours weekly"
    },
    {
        "number": "37",
        "name": "Social Media Manager",
        "filename": "37-Social-Media-Manager.md",
        "purpose": "Manage social media platforms.",
        "responsibilities": [
            "Create content calendar",
            "Post on social platforms",
            "Respond to comments",
            "Moderate discussions",
            "Track engagement metrics",
            "Report on social media",
            "Maintain positive community"
        ],
        "reporting": "Communications Director",
        "time": "3-8 hours weekly"
    },
    {
        "number": "38",
        "name": "Website Administrator",
        "filename": "38-Website-Administrator.md",
        "purpose": "Maintain website content.",
        "responsibilities": [
            "Update website content",
            "Check accessibility",
            "Maintain web forms",
            "Update event pages",
            "Maintain donation links",
            "Track website analytics",
            "Support user experience"
        ],
        "reporting": "Communications Director",
        "time": "2-6 hours weekly"
    },
    {
        "number": "39",
        "name": "Media Coordinator",
        "filename": "39-Media-Coordinator.md",
        "purpose": "Coordinate press and media.",
        "responsibilities": [
            "Maintain media database",
            "Prepare press releases",
            "Schedule media interviews",
            "Create media kits",
            "Verify story consents",
            "Track media coverage",
            "Support communications team"
        ],
        "reporting": "Communications Director",
        "time": "Project-based"
    },
    {
        "number": "40",
        "name": "Legal Advisor",
        "filename": "40-Legal-Advisor.md",
        "purpose": "Advise on legal risks.",
        "responsibilities": [
            "Review contracts",
            "Review waivers",
            "Review policies",
            "Answer compliance questions",
            "Address governance issues",
            "Provide legal guidance",
            "Support risk management"
        ],
        "reporting": "Board or Executive Director",
        "time": "As needed"
    },
    {
        "number": "41",
        "name": "Insurance/Risk Manager",
        "filename": "41-Insurance-Risk-Manager.md",
        "purpose": "Manage insurance and risk.",
        "responsibilities": [
            "Review insurance coverage",
            "Maintain insurance certificates",
            "Coordinate claim reporting",
            "Maintain risk register",
            "Communicate with broker",
            "Track compliance",
            "Report on risk"
        ],
        "reporting": "Legal and Risk Management lead",
        "time": "2-6 hours weekly"
    },
    {
        "number": "42",
        "name": "Safety Coordinator",
        "filename": "42-Safety-Coordinator.md",
        "purpose": "Coordinate safety standards.",
        "responsibilities": [
            "Provide safety training",
            "Review incident trends",
            "Track corrective actions",
            "Develop safety checklists",
            "Monitor safety compliance",
            "Report on safety metrics",
            "Support risk management"
        ],
        "reporting": "Executive Director or Legal lead",
        "time": "3-8 hours weekly"
    }
]

def create_manual(pos):
    """Create position manual content."""
    return f"""# {pos['name']} — Position Manual

## Position Overview

The {pos['name']} position supports Lost Limb Riders in fulfilling its mission to serve amputees, limb-difference individuals, families, caregivers, and allies.

## Core Purpose

{pos['purpose']}

## Primary Responsibilities

""" + "\n".join([f"- {resp}" for resp in pos['responsibilities']]) + f"""

## Time Commitment

{pos['time']}

## Reporting Structure

- Reports to: {pos['reporting']}

## Success Measurements

- Responsibilities are completed effectively and timely
- Stakeholders and community members report positive impact
- Work aligns with organizational mission and values
- Professional standards and safety protocols are maintained
- Team collaboration and communication are strong

## Key Relationships

- **Supervisor:** Regular communication and coordination on performance
- **Peers:** Collaboration on related initiatives and programs
- **Community:** Service to amputee, limb-difference, and caregiver community
- **Partners:** Collaboration with healthcare and community organizations

## Development & Support

- **Orientation:** Comprehensive organizational training on mission and culture
- **Mentoring:** Ongoing support from supervisor and experienced team members
- **Professional Development:** Training opportunities in relevant areas
- **Resources:** Tools, technology, and support needed for role success
- **Performance Review:** Annual review and feedback from supervisor

## Onboarding Checklist

- [ ] Attend organizational orientation and mission training
- [ ] Meet with supervisor and discuss role expectations
- [ ] Review organizational policies and procedures manual
- [ ] Complete required training (safety, confidentiality, background check)
- [ ] Learn role-specific systems and technology
- [ ] Meet team members and cross-functional partners
- [ ] Review this position manual thoroughly
- [ ] Schedule regular check-in meetings with supervisor
- [ ] Ask questions and clarify any unclear expectations

## Position Policies

All employees and volunteers in this position must:

- Maintain commitment to organizational mission and values
- Follow all organizational policies and procedures
- Maintain confidentiality of sensitive information
- Support a safe, respectful, and inclusive environment
- Complete required training and compliance certifications
- Report concerns or safety issues immediately
- Participate in ongoing professional development

---

**Document Version:** 1.0  
**Last Updated:** [Date]  
**Adopted By:** Board of Directors  
**Review Schedule:** Annually or upon significant organizational change  
**Position Status:** Active
"""

def main():
    """Generate all position manual files."""
    
    # Determine output directory
    if len(sys.argv) > 1:
        base_path = sys.argv[1]
    else:
        base_path = "./employees"
    
    # Create directory if it doesn't exist
    os.makedirs(base_path, exist_ok=True)
    
    created = 0
    failed = 0
    
    for pos in POSITIONS:
        filepath = os.path.join(base_path, pos['filename'])
        try:
            content = create_manual(pos)
            with open(filepath, 'w') as f:
                f.write(content)
            print(f"✓ Created: {pos['filename']}")
            created += 1
        except Exception as e:
            print(f"✗ Failed: {pos['filename']} - {str(e)}")
            failed += 1
    
    print(f"\n{'='*60}")
    print(f"Position Manual Generation Complete")
    print(f"{'='*60}")
    print(f"Total Created: {created}")
    print(f"Total Failed: {failed}")
    print(f"Output Directory: {base_path}")
    print(f"Total Positions: {len(POSITIONS)}")

if __name__ == "__main__":
    main()
