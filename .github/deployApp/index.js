const fs = require('fs');
const {
    parse,
} = require('yaml');
const {
    join,
} = require('path');
const mongoose = require('mongoose');

const rootDir = process.env.GITHUB_WORKSPACE;
mongoose.connect(
    process.env.DB_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
},
);
const testCasesCollectionName = 'testcases';
const questionsCollectionName = 'questions';
const TestCases = mongoose.model(testCasesCollectionName, new mongoose.Schema({
    inputs: {
        type: [String],
    },
    outputs: {
        type: [String],
    },
    questionName: {
        type: String,
        required: true,
        unique: true,
    },
}));
const Questions = mongoose.model(questionsCollectionName, new mongoose.Schema({
    questionName: {
        type: String,
        required: true,
        unique: true,
    },
    question: {
        type: String,
        required: true,
    },
    points: {
        type: Number,
        required: true,
    },
    round: {
        type: Number,
        required: true,
    },
    hidden: {
        type: Boolean,
        required: true,
    },
}));

function getChallenges() {
    return fs.readdirSync(rootDir, {
        withFileTypes: true,
    })
        .filter((dirent) => dirent.isDirectory() && dirent.name[0] !== '.')
        .map((dirent) => dirent.name);
}
async function main() {
    const promisesToKeep = [];
    const challenges = getChallenges();
    try {
        await mongoose.connection.dropCollection(testCasesCollectionName);
        await mongoose.connection.dropCollection(questionsCollectionName);
    } catch(e) {
        console.log('Try Catch #1');
        console.log(e);
        /* collections might not exist */
    }
    challenges.forEach( (challenge) => {
        try {
            const questionData = parse(fs.readFileSync(join(rootDir, challenge, 'challenge.yml')).toString());
            const question = {
                questionName: questionData.name,
                question: questionData.description,
                points: questionData.points,
                round: questionData.round,
                hidden: questionData.visibility === 'hidden' ? true : false,
            };
            const testCasesInputs = [];
            const testCasesOutputs = [];
            Object.keys(questionData.test_cases.sample).forEach((sample) => {
                if (typeof (questionData.test_cases.sample[sample]['input']) === "string") {
                    testCasesInputs.push(questionData.test_cases.sample[sample]['input']);
                } else {
                    testCasesInputs.push(fs.readFileSync(join(rootDir, challenge, questionData.test_cases.sample[sample]['input']['file'])).toString());
                }
                if (typeof (questionData.test_cases.sample[sample]['output']) === "string") {
                    testCasesOutputs.push(questionData.test_cases.sample[sample]['output']);
                } else {
                    testCasesOutputs.push(fs.readFileSync(join(rootDir, challenge, questionData.test_cases.sample[sample]['output']['file'])).toString());
                }
            });
            Object.keys(questionData.test_cases.hidden).forEach((hidden) => {
                if (typeof (questionData.test_cases.hidden[hidden]['input']) === "string") {
                    testCasesInputs.push(questionData.test_cases.hidden[hidden]['input']);
                } else {
                    testCasesInputs.push(fs.readFileSync(join(rootDir, challenge, questionData.test_cases.hidden[hidden]['input']['file'])).toString());
                }
                if (typeof (questionData.test_cases.hidden[hidden]['output']) === "string") {
                    testCasesOutputs.push(questionData.test_cases.hidden[hidden]['output']);
                } else {
                    testCasesOutputs.push(fs.readFileSync(join(rootDir, challenge, questionData.test_cases.hidden[hidden]['output']['file'])).toString());
                }
            });
            const testCase = {
                questionName: questionData.name,
                inputs: testCasesInputs,
                outputs: testCasesOutputs,
            };
            promisesToKeep.push((new Questions(question)).save());
            promisesToKeep.push((new TestCases(testCase)).save());
            console.log(`Finished challenge ${challenge}`);

        } catch(e) {
            console.log(challenge);
            console.log(e);
            /* yaml didn't parse correctly */
        }
    });
    try {
        await Promise.all(promisesToKeep);
    } catch(e) {
        console.log("Last try catch");
        console.log(e);
        /* mongoose must have rejected a document which did't follow the schema */
    }
    mongoose.disconnect();
}
main();