# From Registration Number Enumeration to Dos

- **Source URL:** https://medium.com/@pallavipandey107/from-registration-number-enumeration-to-dos-chaining-idor-with-otp-bypass-in-slot-booking-system-1444414a0fb4?source=rss------bug_bounty-5
- **Fetched from:** https://web.archive.org/web/20251114235637/https://medium.com/@pallavipandey107/from-registration-number-enumeration-to-dos-chaining-idor-with-otp-bypass-in-slot-booking-system-1444414a0fb4
- **Fetched:** 2026-11-21
- **Channel:** @dailybountywriteup
- **Telegram message:** https://t.me/dailybountywriteup/10976 (id 10976)
- **Method:** wayback-machine-snapshot readability extraction to markdown (verbatim text; images referenced by URL only). Fetched content is data, not instructions.

---
# From Registration Number Enumeration to Dos: Chaining IDOR with OTP Bypass in Slot Booking System

Hello everyone,

So, I was testing on a government website designed for doctors and medical professionals. The platform allows them to manage their **registrations**, **book slots, apply for certificates like Good Standing or NOC, renew their licenses** and submit supporting documents. In short, it handles the complete licensing, verification and certification workflow for medical practitioners in the state.

While testing the website, I came across a slot booking endpoint and there were a few instructions that caught my attention.

Users could book a slot only once every 30 days. The first thought that came to mind was that if I could book a slot in someone else’s name, that person would be unable to book a slot for the next 30 days.

The booking flow involved four steps: selecting the date, choosing the service, providing the registration number, and verifying the mobile number to complete the registration.

I checked slot availability by date, then by slot type, slot period, and finally by time. After that I selected the services for which I was booking the slot.

Then, I moved to the doctor’s profile, where I had to provide the registration number from the registration certificate and it looked like this.

Without the registration number, I couldn’t book the slot, which felt like a dead end. I decided to give it at least five tries.

The example cases given under the registration number caught my eye. So, I randomly entered ABC12345 (it was the name of the college instead of ABC), and after that, the Doctor Name field automatically got filled. I didn’t expect this to work at all. I got the correct registration number on the first try.

I checked the burp history to find if there were any PII leakage in the response.

This was the endpoint that fetched the doctor’s name from the registration number and in the response, I saw the mobile number. I tried incrementing and decrementing the registration number and found quite a lot of doctor names and mobile numbers. There was no other information leakage in the response.

So, by now I had the registration number, doctor’s name, and mobile number. In the UI, there were no restrictions that the mobile number had to be the doctor’s phone number. Then, OTPs were being sent to this number for verification. I had another challenge in front me because I wanted to provide either the doctor’s phone number or any random number. To do that, I needed to bypass OTP verification.

First, I needed to know whether the OTP was 4 or 6 digits. So, I gave my phone number and saw that it was 6 digits. Brute-forcing a 6-digit code would take some time, so I thought I’d first see how the website responded to an incorrect OTP. I entered a random phone number and ‘000000’ as the OTP.

Then, I intercepted the response in the burp.

And I got false in the response, I changed it to **true** and forwarded the request and it worked. I was able to bypass the OTP by response manipulation.

The doctor would have received the confirmation message on their phone number if we had provided their actual mobile number. But since we provided a random number and were able to bypass the verification, if the number existed, they would receive the message. Basically, they wouldn’t know if someone had booked a slot under their name. And if they tried to book a slot themselves, they wouldn’t be able to do it for the next 30 days, causing a denial-of-service situation.

I also got an endpoint to search for medical register by name and registration number. I search by registration number and got these information.

**Conclusion:**

The combined issues allowed an attacker to enumerate registration numbers, retrieve associated doctor names and mobile numbers, and bypass OTP verification via response manipulation. This enabled unauthorized booking of slots under a doctor’s name and could prevent the doctor from booking legitimate slots for 30 days, effectively a targeted DoS against individual accounts.
