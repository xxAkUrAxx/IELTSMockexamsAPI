const sgMail = require('@sendgrid/mail');

exports.handler = async (event, context) => {
  try {
    const data = JSON.parse(event.body);

   sgMail.setApiKey(process.env.SENDGRID_API_KEY);


    const attachments = [];

    if (data.imageBase64) {
      attachments.push({
        content: data.imageBase64,
        filename: `${data.testName || 'Test'}_${data.studentName || 'Student'}.png`,
        type: 'image/png',
        disposition: 'attachment'
      });
    }

    const msg = {
      to: 'ajlrademeyer@gmail.com',
      from: 'armand.r@wallstreetenglish.la', // Must match the verified sender
      subject: `IELTS Test Results - ${data.studentName || 'Unknown Student'}`,
      text: `New test submission received:\n\n${JSON.stringify(data, null, 2)}`,
      attachments: attachments
    };

    await sgMail.send(msg);

    return {
      statusCode: 200,
      body: JSON.stringify({ success: true, message: 'Results sent successfully!' }),
    };

  } catch (err) {
    console.error('Error sending email:', err);

    return {
      statusCode: 500,
      body: JSON.stringify({ success: false, message: 'Failed to send results.' }),
    };
  }
};

